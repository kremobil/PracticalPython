def print_inventory(inventory: dict) -> None:
    """Prints the inventory to the console"""

    print("Idwetarz:")
    print("\n".join(f"{value} {key}" for key, value in inventory.items()))
    print(f"Całkowita liczba przedmiotów: {sum(inventory.values())}")

def add_to_inventory(inventory: dict, items: list) -> dict:
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inventory = {
    "lina": 1,
    "pochodnia": 6,
    "złote monety": 42,
    "sztylet": 1,
    "strzała": 12,
}

dragon_loot = ["złote monety", "sztylet", "złote monety", "złote monety", "rubin"]

print_inventory(inventory)

inventory = add_to_inventory(inventory, dragon_loot)

print_inventory(inventory)