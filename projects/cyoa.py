"""A Pet Store Game for my first COMP110 Project."""

__author__ = "730395734"  

points: int = 0
player: str
choice: str
pet_choice: str
pet_name: str
job_choice: str
DOG_EMOJI: str = "\U0001F436"
CAT_EMOJI: str = "\U0001F431"
FISH_EMOJI: str = "\U0001F41F"


def main() -> None:
    """Choose to buy a pet, get a job, check points, or leave."""
    global points
    global player
    greet()
    i: int = 1
    while i > 0:
        choice = input(f"{player}, enter 1 to buy a pet, 2 to start job training, 3 to check your points, or 4 to leave! ")
        int_choice: int = int(choice)
        if int_choice == 1:
            buy_pet()
        if int_choice == 2:
            job()
        if int_choice == 3:
            check_points(points)
        if int_choice == 4:
            exit()
    print(f"You earned {points} points!")   
    points = 0
    i = i + 1


def greet() -> None:
    """Greeting Player Function."""
    print("Welcome to Katie's Pet Store! We have pets for adoption and we are hiring!")
    global player
    player = input("What is your name? ")


def buy_pet() -> None: 
    """Choose pet function."""
    global points
    points = points + 5 
    pet_choice = input(f"Enter 1 to adopt a dog, 2 for a cat, or 3 for a fish, {player}? ")
    int_pet_choice: int = int(pet_choice)
    points = points + 5
    if int_pet_choice == 1:
        pet_name: str = input(f"What are you going to name your {DOG_EMOJI}? ")
    if int_pet_choice == 2:
        pet_name: str = input(f"What are you going to name your {CAT_EMOJI}? ")
    if int_pet_choice == 3:
        pet_name: str = input(f"What are you going to name your {FISH_EMOJI}? ")
    points = points + 5
    print(f"Don't forget to buy some supplies for {pet_name}! Have a great day!")


def job() -> None: 
    """Choose job game."""
    global points
    points = points + 5 
    print(f"We're shortstaffed, so you get the job, {player}!")
    job_choice = input("Do you want to be a cashier or an animal caretaker? ")
    points = points + 5
    print(f"Welcome to the team, {player} as our newest {job_choice}!")
    from random import randint
    random_pay: int = randint(1, 10)
    print(f"You are going to start with an hourly pay of {random_pay}!")
    print("See you tomorrow for training!")


def check_points(points) -> int:
    """Check points and double them."""
    point_counter = input(f"{player}, enter 1 to check your points or 2 to return to the game. ")
    point_counter_int: int = int(point_counter)
    if point_counter_int == 1:
        print(f"You earned {points} points and we are doubling them since you are such a great player!")
        points = points * 2
        
    return points


def exit() -> None:
    """Exit the game."""
    global player
    global points
    print(f"Goodbye, {player}! You earned {points} points!")


if __name__ == "__main__":
    main()
