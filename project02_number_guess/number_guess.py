import random

def computer_choice():
    # Returns a random integer between 1 and 20 (inclusive)
    return random.randint(1,20)

def user_choice():
    # Prompts the user for their name and guess, returns guess
    name = input("\nWhat's your name? ")
    print(f"\nHello {name}, nice to meet you! I have picked a number from 1 to 20.\nI would love it if you could make a guess!")
    while True:
        try:
            guess = int(input(f"\n{name}, enter your guess between 1 and 20: "))
            return guess
        except ValueError:
            print("Please enter a valid integer between 1 and 20.")

def list_of_random_msg(comp_choice):
    # Returns a random congratulatory message using the correct number
    msgs = [
        f"You definitely are a magician! You guessed {comp_choice} correctly. Congratulations!",
        f"Wow! {comp_choice} was the number, and you nailed it! You're on fire!",
        f"Impressive! {comp_choice} was my secret number, and you found it!",
        f"Spot on! {comp_choice} is exactly what I picked. Well done!",
        f"Amazing guess! {comp_choice} was the number I had in mind. You must be psychic!",
        f"Bravo! {comp_choice} was the answer, and you got it right!",
        f"Outstanding! You guessed {comp_choice} perfectly. You have a sharp mind!",
        f"Fantastic! {comp_choice} was the number, and you guessed it without a hitch!",
        f"Superb! {comp_choice} was my choice, and you discovered it!",
        f"Incredible! {comp_choice} was the number, and you guessed it like a pro!",
        f"You have a sixth sense! {comp_choice} was the number, and you got it!"
    ]
    return random.choice(msgs)

def main_logic():
    # Main game logic for one round
    comp_choice = computer_choice()  # Computer selects a number
    guess = user_choice()            # User makes a guess
    equal_choice = (guess == comp_choice)  # Check if guess is correct
    diff = abs(guess - comp_choice)        # Difference between guess and actual number
    if 1 <= guess <= 20:
        if equal_choice:
            # Correct guess
            print(f"Well done! You beat me in one go. Your guess of {comp_choice} was correct, which has a 5% chance.")
            msg = list_of_random_msg(comp_choice)
            print(msg)
        elif 0 < diff <= 2:
            # Very close guess
            print(f"You were so close! Try again. My number was {comp_choice}.")
        elif 3 <= diff <= 5:
            # Somewhat close guess
            print(f"You were a bit off. Try again! My number was {comp_choice}.")
        elif diff > 5:
            # Far off guess
            print(f"You were too far off. Try again! My number was {comp_choice}.")
    else:
        # Guess out of valid range
        print("Please Enter the number between 1 - 20")

while True:
    try:
        # Print welcome message and start a round
        print("-" * 60, "Welcome to the Number Guess Game", "-" * 60)
        main_logic()
        # Ask user if they want to continue
        ask = input("\nDo you Wish to Continue? (1=Yes, 0=No) ")
        if ask.strip() == "0":
            break
        elif ask.strip() != "1":
            print("Please enter a valid choice!")
    except ValueError:
        # Handle invalid input
        print("Please enter a valid choice!")