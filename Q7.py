#Roll the dice
import random

def roll_dice(num_dice=1, num_sides=6):
    if num_dice <= 0 or num_sides <= 0:
        return "Invalid input! Number of dice and number of sides must be positive integers."
    
    results = []
    for _ in range(num_dice):
        roll_result = random.randint(1, num_sides)
        results.append(roll_result)
    
    return results

def main():
    print("Welcome to Roll the Dice!")
    num_dice = int(input("Enter the number of dice to roll: "))
    num_sides = int(input("Enter the number of sides for each die: "))
    
    dice_results = roll_dice(num_dice, num_sides)
    print("Results:", dice_results)

if __name__ == "__main__":
    main()
