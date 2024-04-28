#Inventary System
import random
def hdn4wrd_purchase(item, price, amount):
    total_cost = price * amount
    return total_cost

def rv3rse_change(given, total_cost):
    return given - total_cost

def v3rt1c4l_count_notes(change):
    notes = [500, 200, 100, 50, 10, 5, 2, 1]
    notes_count = {}

    for note in notes:
        count = change // note
        if count > 0:
            notes_count[note] = count
            change %= note

    return notes_count

def inventory_system():
    inventory = {
        "item1": 10,
        "item2": 20,
        "item3": 15
    }

    while True:
        print("\nAvailable Items:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

        item = input("\nEnter the item you want to purchase: ")
        if item not in inventory:
            print("Item not available! Please choose again.")
            continue

        price = random.randint(5, 100)
        amount = int(input(f"Enter the quantity of {item} you want to buy: "))
        total_cost = hdn4wrd_purchase(item, price, amount)

        print(f"Total cost for {amount} {item}: {total_cost}")

        given = float(input("Enter the amount given: "))
        change = rv3rse_change(given, total_cost)

        if change < 0:
            print(f"You still need to pay {-change} more.")
        elif change == 0:
            print("Exact amount given. Thank you!")
        else:
            print(f"Change to be returned: {change}")
            notes_count = v3rt1c4l_count_notes(change)
            print("Number")
