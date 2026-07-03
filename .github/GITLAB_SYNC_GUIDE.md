# GitHub → GitLab sync setup

This file documents the automation that keeps this project's GitLab mirror
(`https://gitlab.amcbridge.com/asirchenko/freecad-manual-to-automation-sandbox`)
in sync with GitHub (`https://github.com/asirchenko/freecad-manual-to-automation-sandbox`).

**This file must stay inside `.github/`.** Everything under `.github/` is
intentionally excluded from what gets pushed to GitLab (see "How the sync
works" below), so this doc — and the workflow itself — never shows up for
anyone who views the GitLab project.

## Why this exists

Work happens from two laptops:
- **Autodesk laptop** — GitHub access only.
- **AMC laptop** — GitHub *and* GitLab access.

Goal: push to GitHub from either laptop, and have GitLab automatically end up
with the same project content, without manual steps on the AMC laptop.

## Why not GitLab's built-in Pull Mirroring?

GitLab repository mirroring supports two directions: **Push** (GitLab →
elsewhere) and **Pull** (elsewhere → GitLab). Pull mirroring is what we'd
want here, but on `gitlab.amcbridge.com` the Direction selector is locked to
Push and disabled — **Pull mirroring requires a GitLab Premium/Ultimate
license**, which this instance doesn't have. So GitLab can't be told to pull
from GitHub on its own; something has to push *to* GitLab instead.

## Architecture

```
GitHub push (any laptop)
   -> GitHub Actions workflow triggers (.github/workflows/gitlab-mirror-sync.yml)
   -> runs on a self-hosted runner installed on the AMC laptop
   -> runner clones the fresh GitHub content, strips .git and .github
   -> commits it as a single new commit, force-pushes to GitLab main
```

The self-hosted runner is required because `gitlab.amcbridge.com` only
resolves on the AMC corporate network — GitHub's own cloud runners
(`ubuntu-latest` etc.) get DNS resolution failures trying to reach it.

## Components

### 1. Self-hosted GitHub Actions runner (AMC laptop)

- Install directory: `D:\actions-runner`
- Registered against this repo with label `amc-laptop`
- Installed as a Windows service so it runs even when nobody is logged in
  interactively:
  - Service name: `actions.runner.asirchenko-freecad-manual-to-automation-sandbox.ASIRCHENKO`
  - Runs as: `NT AUTHORITY\NETWORK SERVICE`
  - Start type: Automatic

To check its status:
```powershell
Get-Service "actions.runner.asirchenko-freecad-manual-to-automation-sandbox.ASIRCHENKO"
```

To reinstall/re-register it from scratch (e.g. token expired, moved
machines):
```powershell
cd D:\actions-runner
.\config.cmd remove --token <removal-token-from-GitHub-Settings-Actions-Runners>
.\config.cmd --unattended --url https://github.com/asirchenko/freecad-manual-to-automation-sandbox --token <new-registration-token> --labels amc-laptop --runasservice
```
`--runasservice` requires an **elevated (Administrator) PowerShell window** —
it fails silently otherwise with "Needs Administrator privileges".
Registration/removal tokens come from GitHub: Settings → Actions → Runners →
"New self-hosted runner" (for a new token) or the runner's "..." menu (to
remove).

### 2. GitHub Actions workflow

File: `.github/workflows/gitlab-mirror-sync.yml`

Triggers on every push to any branch, plus manual `workflow_dispatch`. Runs
only on `[self-hosted, Windows]`.

Two non-obvious things baked into the workflow:
- `shell: powershell -ExecutionPolicy Bypass -Command ". '{0}'"` — the
  runner's default PowerShell execution policy blocks running the
  auto-generated step script, so this bypasses it for just this step.
- `git config user.name` / `user.email` set explicitly inside the script —
  the `NETWORK SERVICE` account has no git identity configured, so
  `git commit` would otherwise fail with "Please tell me who you are".

### 3. GitHub secret: `GITLAB_MIRROR_TOKEN`

- Where: GitHub repo → Settings → Secrets and variables → Actions →
  Repository secrets (not the account-level Settings page — easy to look in
  the wrong place).
- Value: a GitLab **Project Access Token** created in GitLab under
  Settings → Access Tokens, with:
  - Role: **Maintainer**
  - Scope: **api** (or at minimum `write_repository`, since it's only used
    to `git push`)
- Used as the HTTP password when pushing: `https://oauth2:<token>@gitlab.amcbridge.com/...`
  (username can be any non-empty string for token auth; `oauth2` is just a
  placeholder).
- Rotate it by creating a new Project Access Token in GitLab and updating
  the secret value in GitHub — no other change needed.

### 4. GitLab: "Allow force push" on `main`

Because the sync always rewrites GitLab's history to a single fresh commit
(see below), it needs a force push every time. GitLab protected branches
reject force pushes by default. Enabled at:
Settings → Repository → Branch rules → `main` → **Allow force push** toggle.

## How the sync works (current script logic)

Every run does the same four things, unconditionally:
1. `git clone --depth 1` the current GitHub `main` into a temp folder.
2. Delete `.git` and `.github` from that folder — so no GitHub git history
   and no trace of this workflow/automation is included.
3. `git init` a brand-new repo in that folder, commit everything with the
   fixed message `"Sync current project state"` (never GitHub's actual
   commit message — deliberately neutral/generic).
4. `git push --force` that single commit as GitLab's `main`.

Net effect: **GitLab's `main` always has exactly one commit**, reflecting
the current GitHub content minus `.github/`, authored with a generic
message. There is no incremental history on the GitLab side by design — this
was chosen specifically so nobody looking at the GitLab project can see any
sign of GitHub Actions, tokens, runners, or the sync mechanism itself.

## How to verify it's working

Via GitHub: Actions tab → "Sync to GitLab" workflow → latest run should be
green.

Via GitHub API (no auth needed for a public repo):
```
GET https://api.github.com/repos/asirchenko/freecad-manual-to-automation-sandbox/actions/runs?per_page=1
```

Via GitLab API (needs a token with at least `read_api` scope):
```powershell
$headers = @{ "PRIVATE-TOKEN" = "<your-gitlab-token>" }
$projectId = [uri]::EscapeDataString("asirchenko/freecad-manual-to-automation-sandbox")
Invoke-RestMethod -Uri "https://gitlab.amcbridge.com/api/v4/projects/$projectId/repository/commits" -Headers $headers
```
Expect exactly one commit, titled "Sync current project state".

## Known pitfalls hit while setting this up (for future reference)

- **GitHub-hosted runners can't reach `gitlab.amcbridge.com`** — DNS only
  resolves inside the AMC network. Symptom: `curl: (6) Could not resolve
  host`. Fix: self-hosted runner on a machine inside that network.
- **GitLab returns HTTP 404 (not 401/403) for bad/missing auth or a
  nonexistent mirror** — makes remote diagnosis ambiguous. If you see 404
  from a GitLab API call, check both the token *and* whether the thing
  you're calling actually exists/is configured.
- **Pull mirroring is Premium/Ultimate-only** — don't waste time trying to
  configure Direction=Pull on a Free/Core-tier GitLab instance; it'll be
  greyed out.
- **PowerShell execution policy** blocks the runner's generated step
  scripts by default — needs the `-ExecutionPolicy Bypass` shell override
  shown above.
- **`NETWORK SERVICE` has no git identity** — `git commit` fails without
  explicitly setting `user.name`/`user.email` first.
- **Protected branches reject force pushes by default** — needed to enable
  "Allow force push" in GitLab for this workflow's approach to work.
