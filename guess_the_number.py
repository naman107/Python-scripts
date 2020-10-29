import random as rd

#Make variables as simple as possible
attempts = 5
def guess_it(attempts):
    print("Let's play a guessing number game! Guess a number. You only have (5) attempts!!!")
    random_number = rd.randint(1, 50)
    while True:
        print(f"Available attempts: {attempts}")
        if(attempts > 0):
            user_number=input('Enter the number -> ')

            #input return a string so surround it with int
            if(int(user_number) < random_number):
                print(f"Try a number higher than {user_number}")
                attempts = attempts-1
            elif(int(user_number) > random_number):
                print(f"Try a number lower than {user_number}")
                attempts = attempts-1
            else:
                print('Yes, You won!')
                return
        else:
            print('Sorry, you lost!')
            return

#call the function
guess_it(attempts)


#Guys don't stop here. Do make it more complex and maybe convert it to a real game.