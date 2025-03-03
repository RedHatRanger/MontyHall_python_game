import random

def monty_hall_game():
    print("\nWelcome to the Monty Hall Game!")
    print("Behind one door is a brand new RED CONVERTIBLE CAR!")
    print("Behind the other two doors are goats.\n")
    
    # Define the three doors
    doors = [1, 2, 3]
    
    # Randomly place the car behind one door
    car_door = random.choice(doors)
    
    # Player makes an initial choice
    while True:
        try:
            player_choice = int(input("Choose a door (1, 2, or 3): "))
            if player_choice in doors:
                break
            else:
                print("Please choose a valid door number: 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Enter a number (1, 2, or 3).")
    
    # Host opens a door that is not the player's choice and not hiding the car
    remaining_doors = [door for door in doors if door != player_choice]
    # Filter out any door that has the car if player's choice isn't the car
    possible_doors_to_open = [door for door in remaining_doors if door != car_door]
    
    # If the player's initial choice is the car, host randomly selects one of the remaining doors
    if not possible_doors_to_open:
        possible_doors_to_open = remaining_doors
    
    revealed_door = random.choice(possible_doors_to_open)
    print(f"\nThe host opens door {revealed_door} revealing a goat!")
    
    # Ask the player if they want to switch
    while True:
        switch = input("Do you want to switch to the other unopened door? (yes/no): ").lower().strip()
        if switch in ['yes', 'y', 'no', 'n']:
            break
        else:
            print("Please answer 'yes' or 'no'.")
    
    if switch in ['yes', 'y']:
        # Switch: the new choice is the remaining door that's neither the player's original nor the revealed door
        new_choice = [door for door in doors if door != player_choice and door != revealed_door][0]
        print(f"You switched from door {player_choice} to door {new_choice}.")
        player_choice = new_choice
    else:
        print(f"You stick with your original choice, door {player_choice}.")
        
    # Reveal the final result
    print("\nFinal reveal...")
    if player_choice == car_door:
        print("Congratulations! You won the brand new RED CONVERTIBLE CAR!")
    else:
        print("Sorry, you got a goat!")
    
    print(f"The car was behind door {car_door}.\n")

if __name__ == "__main__":
    monty_hall_game()
