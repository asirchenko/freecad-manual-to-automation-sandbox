"""Week 2 — Part 3: Loops (циклы)."""

# --- for по списку строк (списки подробнее в Week 3) ---
menu_items = ["File", "Edit", "View", "Tools"]

print("Main menu items:")
for item in menu_items:
    print(f"  - {item}")

# --- for + range (повторить N раз) ---
print("\nRetry attempts:")
for attempt in range(1, 4):
    print(f"  Attempt {attempt}/3")

# --- while — ждём условие ---
print("\nSimulated wait for window:")
seconds_left = 3
while seconds_left > 0:
    print(f"  Waiting... {seconds_left}s")
    seconds_left -= 1
print("  Window ready")

# --- break — выход из цикла раньше времени ---
print("\nSearch for open document:")
documents = ["Start", "Start", "Unnamed", "Box"]

for name in documents:
    if name == "Unnamed":
        print(f"  Found document: {name}")
        break
    print(f"  Skipping: {name}")

# --- YOUR TURN ---
# Выведите числа 1, 2, 3, 4, 5 каждое с новой строки через for + range
print("\nCount 1 to 5:")
for n in range(1, 6):
    print(n)
