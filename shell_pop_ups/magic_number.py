import random

print("Hello, what is your name?")
name = input()

print("Hello, " + name)

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "your user number is between{0} and {1}"
print(message.format(minNumber, maxNumber))

found = False

while not found:
    print("Guess what it is?")
    guess = int(input())

    if guess == magicNumber:
        found == True
        print("***")
        break
    if guess < magicNumber:
        print("Too low")
    if guess > magicNumber:
        print("Too high")
    

        
print("You got it!")



    
