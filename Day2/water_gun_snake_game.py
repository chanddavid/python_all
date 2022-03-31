# snake,water,gun game
from random import randint
import random

rand=random.randint(0,2)
user=input("Please Enter snake(s),water(w) gun(g):")

print(rand)

if rand==0:
    comp='s'
elif rand==1:
    comp='w'
else:
    comp='g'

def game(user,comp):
    if user==comp:
        print("Game Draw")
    elif user=='w' and comp=='s':
        print("You lose")
    elif user=='w' and comp=='g':
        print("You win")
    elif user=='g' and comp=='s':
        print("You win")
    elif user=='g' and comp=='w':
        print("You lose")
    elif user=='s' and comp=='w':
        print("You win")
    elif user=='s' and comp=='g':
        print("You lose")

 

print("you choose",user)
print("comp choose",comp)