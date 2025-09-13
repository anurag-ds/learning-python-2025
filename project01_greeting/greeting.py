import random
def user_input():
    global name
    name = input("\nEnter your Name: ")
    global age 
    age = int(input("\nEnter your age: "))
    global hobby
    hobby = input("\nEnter your Hobby(if more than one write by seperating them with a space) : ")

def list_of_greet(age, name, hobby):
    if age >= 5 and age <= 100:
        if age >= 18:
            motivational = "Keep inspiring others with your maturity and passion!"
            return [
                f"\nDear {name}, Good Morning! At {age}, having hobbies like {hobby} is such a great thing. {motivational}\n",
                f"\nHope you have a great day ahead, {name}. Remember, your age is {age}\n and the hobbies you have, like {hobby}, are pretty impressive at that age. {motivational}\n",
                f"\nHey there! Your current age is {age}\n and your hobbies are {hobby}. That's something to be proud of, {name}. {motivational}\n",
                f"\nEnjoy your day, {name}. What's on your list? Is it {hobby}? Well, at {age},\n you must be energetic! {motivational}\n",
                f"\nYou need to be jailed, {name}, for looking this good at {age}. That's obviously a 'WOW' factor.\n So, are you doing great with {hobby}? {motivational}\n"
            ]

        else:
            motivational = "Your youth is your strength—dream big and keep growing!"
            return [
                f"\nDoing great, {name}. Note your age is {age}\n and your current hobbies are {hobby}. You don't have much time,\n so be fast and show the world the real you—a successful person. {motivational}\n",
                f"\nHey {name}, where did you get that from? Is it from the hobbies you do, like {hobby},\n or is it your age, {age}, speaking? Your smile has filled the room with positive vibes! {motivational}\n",
                f"\nI want a role model like you, {name}, because at the age of {age}\n you have quite a few hobbies, for instance {hobby},\n which make you stand out! {motivational}\n",
                f"\nYou look so good, {name}, even at the age of {age}.\n Might it be due to {hobby}? {motivational}\n",
                f"\nDon't tell me your age is {age}, as it's illegal to be so good and kind! You are so generous, {name}. Just remember,\n don't lose your hobbies like {hobby},\n as that's a gem. If you have that,\n value it and stay happy! {motivational}\n"
            ]
    else:
        print("\nPlease enter a valid age make sure it's greater than 4 and less than 100!")
        return []  # Will return an empty list if the constraint isn't satisfied, so that the function doesn't return 'None'

def main():
    user_input()
    greeting = list_of_greet(age, name, hobby)
    if not greeting:
        return # Exit the main function if the function "list_of_greet()" returns an empty list to the 'greeting' variable to avoid unexpected errors!
    choice = random.choice(greeting)
    print("="*100)
    print(choice)
    print("="*100)

def process():
    exit_choice = int(input("\nWish to Continue?(1[Yes]/0[No]) "))
    return not exit_choice

while 1:
    try:
        print("\n","-"*50,"Personalize Greeting System","-"*50)
        main()
        if process(): break
    except ValueError:
        print("\nPlease Enter a Valid Age!")
        if process(): break