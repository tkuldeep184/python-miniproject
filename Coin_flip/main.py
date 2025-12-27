from logic import flip_coin, roll_die, roll_two_dice
from animations import coin_animation, dice_animation

def show_menu():
    print("Welcome to the Coin Flip and Dice Roll Simulator!")
    print("1. Flip a Coin")
    print("2. Roll a Die")
    print("3. Roll Two Dice")
    print("4. Exit")
    
while True:
    show_menu()
    choice = input("Choose an option (1-4):")
    
    if choice == '1':
        coin_animation()
        result = flip_coin()
        print(f"The coin landed on: {result}")
        
    elif choice == '2':
        dice_animation()
        result = roll_die()
        print(f"You rolled a: {result}")
    
    elif choice == '3':
        dice_animation()
        result1, result2 = roll_two_dice()
        print(f"You rolled: {result1} and {result2}")
    
    elif choice == '4':
        print("Thank you for using the simulator. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
        
    input("Press Enter to continue...")