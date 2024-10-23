import random

def guess_number_game():
    print("Welcome to 'Guess the Number' game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it correctly.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            return
        
        print(f"Attempts remaining: {max_attempts - attempts}")
    
    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number_game()
