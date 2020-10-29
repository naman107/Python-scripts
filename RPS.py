import random

# rock = 1
# paper = 2
# scissors = 3

def comp_chance():
    rand_item = random.randint(1, 3)
    return rand_item

def user_chance():
    user_entry = input("""
        Enter 1 for ROCK
        Enter 2 for PAPER
        Enter 3 for SCISSORS
    """)
    if(not user_entry.isnumeric()):
        # return int(user_entry)
        print('1,2 or 3 are expected')
    # else:
    #     print('1,2 or 3 are expected')

def play():
    # rock = 1
    # paper = 2
    # scissors = 3
    user_entry = input("""
        Enter 1 for ROCK
        Enter 2 for PAPER
        Enter 3 for SCISSORS
    """)
    if(not user_entry.isnumeric()):
        print('1,2 or 3 is expected')
        return
    while True:
        comp = comp_chance()
        print(comp)
        if user_entry == 1:
            if comp == 1:
                print('A tie')
            elif comp == 2:
                print(f"You won! as computer chose ROCK")
                return
            else:
                print('You lose! oops')
                return
        elif user_entry == 2:
            if comp == 1:
                print('You lose! oops')
                return
            elif comp == 2:
                print('A tie')
            else:
                print(f"You won! as computer chose PAPER")
                return
        else:
            if comp == 1:
                print('You lose! oops')
                return
            elif comp == 2:
                print(f"You won! as computer chose SCISSORS")
                return
            else:
                print('A tie')

play()