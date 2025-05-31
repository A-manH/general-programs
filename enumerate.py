fruits = [
    "apple", "banana", "cherry", "apple",
    "banana", "fig", "grape", "fig",
    "kiwi", "lemon", "mango", "kiwi",
    "orange", "papaya", "quince", "papaya",
    "strawberry", "tangerine", "apple", "banana"
]

fruit_map = {fruit: [] for fruit in set(fruits)}
for i, fruit in enumerate(fruits):
    fruit_map[fruit].append(i)
print(fruit_map)