import random
# random()- Return random float between 0.0 and 1.0
#  randint()- return random int between a nd b 
#  choice()- return a random item from the sequence

# fruits=['apple','banana','chiku']
# print(random.random()) 
# print(random.randint(20,25))
# print(random.choice(fruits))

## """"Create a program that roll a dice randomly"""""
 
a="Click"
print("Welcome to tha game :)")
while True:
    choice=input("Type 'Click' To roll the dice or 'q' tp quit:")
    if choice == a:
        number=random.randint(1,6)
        print(f" The no u got is: {number}")
    elif choice == 'q':
        print("Thanks For Playing The game")
    else:
        print("INVALID INPUT")