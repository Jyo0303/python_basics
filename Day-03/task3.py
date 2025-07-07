import random
num=random.randint(1,10)
attempt=1
guess=int(input("Guess the number (1-10): "))
while guess!=num:
    if(guess<num):
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempt+=1
    guess=int(input("Guess the number (1-10): "))
print("Correct! You won in ",attempt,"tries.")
