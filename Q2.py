#Number System (forward, Backward, Horizontal, Vertical)
import random

def forward(num):
    return num + 1

def backward(num):
    return num - 1

def horizontal(num):
    return num * 2

def vertical(num):
    return num / 2

def generate_random_number():
    return random.randint(1, 100)

def number_system():
    current_number = generate_random_number()
    
    print("Welcome to the Number System!")
    print("You are currently at:", current_number)

    while True:
        print("\nChoose your movement:")
        print("1. Forward")
        print("2. Backward")
        print("3. Horizontal")
        print("4. Vertical")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            current_number = forward(current_number)
        elif choice == '2':
            current_number = backward(current_number)
        elif choice == '3':
            current_number = horizontal(current_number)
        elif choice == '4':
            current_number = vertical(current_number)
        elif choice == '5':
            print("Exiting the Number System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

        print("You are now at:", current_number)

number_system()
