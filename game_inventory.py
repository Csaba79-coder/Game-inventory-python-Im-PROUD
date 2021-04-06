from collections import Counter
import csv
from csv import DictReader
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def main():
    inventory = {'rope': 1, 'torch': 6}   
    display_inventory(inventory)
    # print(inventory)
    added_items = ["rope", "rope", "gold coin"]
    add_to_inventory(inventory, added_items)
    # print(inventory)
    removed_items = ["rope", "rope", "gold coin", "silver coin"]
    remove_from_inventory(inventory, removed_items)
    print_table(inventory, "count, desc")
    # print(inventory)
    import_inventory(inventory, filename ="test_inventory.csv")
    # print(inventory)
    export_inventory(inventory, filename="test_export_inventory.csv")
    # print(inventory)

def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    # print("\nInventory of 2021: \n")
    for item in inventory:
        print((f"{item}: {str(inventory[item])}")) # as print put \n I had to remove it! instead of print, I used return


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item not in inventory:
            return  
        if item in inventory:
            inventory[item] -= 1
        if inventory[item] <= 0:
            inventory.pop(item,None)       


def print_table(inventory, order=None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    dash = '-' * 17
    pipe = '|'
    first_column = 'item name'
    second_column = 'count'
    sorted_inventory = {}

    ''' 
    sort by value - first swap the key value pair
    then convert tuple to dict again
    '''
    if order == 'count,asc':
        temp_inventory_tuple = sorted(inventory.items(), key=lambda x: x[1])
        for item in temp_inventory_tuple:
            sorted_inventory[item[0]] = item[1]

    elif order == 'count,desc':
        temp_inventory_tuple = sorted(inventory.items(), reverse=True, key=lambda x: x[1])
        for item in temp_inventory_tuple:
            sorted_inventory[item[0]] = item[1]

    else:
        sorted_inventory = inventory

    print(dash)
    print('{:>9s} {} {:>5s}'.format(first_column, pipe, second_column))
    print(dash)

    for item in sorted_inventory:
        print('{:>9s} {} {:>5s}'.format(item, pipe, str(sorted_inventory.get(item))))

    print(dash)
    

def import_inventory(inventory, filename="test_inventory.cs"):
    """Import new inventory items from a CSV file."""
    items_to_add = []

    try:
        with open(filename, "r") as new_items:
            for line in new_items:
                line = line.replace(", ", ",")
                line = line.split("\n")[0]
                items_to_add = items_to_add + line.split(",")
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return
    add_to_inventory(inventory, items_to_add)
    return inventory


def export_inventory(inventory, filename="test_export_inventory.csv"):
    """Export the inventory into a CSV file."""
    if inventory:
        write_it = ""
        for key, value in inventory.items():
            write_it += ("," + key) * value
        try:
            with open(filename, "w") as save_inventory:
                save_inventory.write(write_it[1:])
        except PermissionError:
            print(f"You don't have permission creating file '{filename}'!")
            return inventory


if __name__ == "__main__":
    main()