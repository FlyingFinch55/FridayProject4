#Powerball Program
import random

print("Welcome to the Powerball number generator.")

# Ask the user if they want to get Powerball numbers
user_input = input("Would you like to generate Powerball numbers? (Enter 'yes' or 'no'): ")

# Check the user's input
if user_input.lower() == 'yes':
    print("Great! Here are your Powerball numbers:")
    
    # Generate five random numbers between 1 and 69
    white_balls = [random.randint(1, 69) for _ in range(5)]
    
    # Generate one random number between 1 and 26 for the Powerball
    powerball = random.randint(1, 26)
    
    # Print the generated numbers
    print("White Balls:", white_balls)
    print("Powerball:", powerball)
    
    # Print a thank you message
    print("Thank you for stopping by!")

else:
    print("Maybe next time! Feel free to come back when you're ready to generate Powerball numbers.")