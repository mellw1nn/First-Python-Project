import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)# Random number between 1 and 100
    attempts = 0# Number of attempts made
    max_attempts = 10# Maximum attempts allowed

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")# Instructions

    while attempts < max_attempts:# Loop until max attempts are reached
        try:# Error handling for non-integer inputs
            guess = int(input("Make a guess: "))# Get user input
            attempts += 1# Increment attempt count

            if guess < 1 or guess > 100:# Validate input range
                print("Please guess a number within the range of 1 to 100.")
                continue# Skip to next iteration if out of range

            if guess < number_to_guess:# Provide feedback
                print("Too low!")
            elif guess > number_to_guess:# Provide feedback
                print("Too high!")
            else:# Correct guess
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:# Handle non-integer input
            print("Invalid input. Please enter a number.")

    if attempts == max_attempts and guess != number_to_guess:# If max attempts reached without correct guess
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")# Reveal the number

guess_the_number()