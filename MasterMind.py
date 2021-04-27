import random

count = 0

numberOne = random.randint(0, 9)
numberTwo = random.randint(0, 9)
numberThree = random.randint(0, 9)
numberFour = random.randint(0, 9)

print(str(numberOne) + " " + str(numberTwo) + " " + str(numberThree) + " " + str(numberFour))

inputNumber = input("Please input a Number from 0 0 0 0 - 9 9 9 9: ")

inpNumberOne, inpNumberTwo, inpNumberThree, inpNumberFour = inputNumber.split(" ")

#1

if str(inpNumberOne) == str(numberOne):
    count += 1

if str(inpNumberTwo) == str(numberTwo):
    count += 1

if str(inpNumberThree) == str(numberThree):
    count += 1

if str(inpNumberFour) == str(numberFour):
    count += 1

#2

if str(inpNumberOne) == str(numberFour):
    count += 1

if str(inpNumberTwo) == str(numberOne):
    count += 1

if str(inpNumberThree) == str(numberTwo):
    count += 1

if str(inpNumberFour) == str(numberThree):
    count += 1

#3

if str(inpNumberOne) == str(numberThree):
    count += 1

if str(inpNumberTwo) == str(numberFour):
    count += 1

if str(inpNumberThree) == str(numberOne):
    count += 1

if str(inpNumberFour) == str(numberTwo):
    count += 1

#4

if str(inpNumberOne) == str(numberTwo):
    count += 1

if str(inpNumberTwo) == str(numberThree):
    count += 1

if str(inpNumberThree) == str(numberFour):
    count += 1

if str(inpNumberFour) == str(numberOne):
    count += 1

print(count)

if count > 3:
    print("Yay you did it woo yay shush")
