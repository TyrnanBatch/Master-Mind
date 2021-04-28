import random

count = 0
stop = 1

numberOne = random.randint(0, 9)
numberTwo = random.randint(0, 9)
numberThree = random.randint(0, 9)
numberFour = random.randint(0, 9)

while stop < 2:
    inputNumber = input("Please input a Number from 0 0 0 0 - 9 9 9 9: ")
    inpNumberOne, inpNumberTwo, inpNumberThree, inpNumberFour = inputNumber.split(" ")    
    if str(inpNumberOne) == str(numberOne):
        count += 1
    elif str(inpNumberOne) == str(numberTwo):
        count += 1
    elif str(inpNumberOne) == str(numberThree):
        count += 1
    elif str(inpNumberOne) == str(numberFour):
        count += 1
    if str(inpNumberTwo) == str(numberOne):
        count += 1
    elif str(inpNumberTwo) == str(numberTwo):
        count += 1
    elif str(inpNumberTwo) == str(numberThree):
        count += 1
    elif str(inpNumberTwo) == str(numberFour):
        count += 1
    if str(inpNumberThree) == str(numberOne):
        count += 1
    elif str(inpNumberThree) == str(numberTwo):
        count += 1
    elif str(inpNumberThree) == str(numberThree):
        count += 1
    elif str(inpNumberThree) == str(numberFour):
        count += 1
    if str(inpNumberFour) == str(numberOne):
        count += 1
    elif str(inpNumberFour) == str(numberTwo):
        count += 1
    elif str(inpNumberFour) == str(numberThree):
        count += 1
    elif str(inpNumberFour) == str(numberFour):
        count += 1
    print(count)
    count = 0


if count == 4:
    print("Yay you did it woo yay shush")
    stop += 2
