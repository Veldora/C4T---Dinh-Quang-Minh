inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["pocket"] = None

print("1) Add a key to inventory called 'pocket':")
print()
for i in inventory:
    print(i, ":", inventory[i])
print()
print()
print()

inventory["pocket"] = ["seashell", "strange berry", "lint"]

print("2) Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint':")
print()
for i in inventory:
    print(i, ":", inventory[i])
print()
print()
print()

inventory["backpack"].remove("dagger")

print("3) Remove('dagger') from the list of items stored under the 'backpack' key:")
print()
for i in inventory:
    print(i, ":", inventory[i])
print()
print()
print()

inventory["gold"] += 50

print("4) Add 50 to the number stored under the 'gold' key:")
print()
for i in inventory:
    print(i, ":", inventory[i])
print()
print()
print()

