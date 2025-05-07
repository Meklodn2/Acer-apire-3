import random

def guess_the_number():
    # Choose difficulty level
    print("Welcome to Guess the Number!")
    print("Choose a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Hard (5 attempts)")
    
    while True:
        level = input("Enter 1 for Easy or 2 for Hard: ")
        if level == '1':
            max_attempts = 10
            break
        elif level == '2':
            max_attempts = 5
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    # Generate the random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print(f"\nI'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it!")
    
    # Game loop
    while attempts < max_attempts:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Check if the player is out of attempts
        if attempts == max_attempts:
            print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

guess_the_number()






# O'yini jovobini chiqarib qo'yish
# O'yin tugagandan kryin davom etitish ha/yo'q

