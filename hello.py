import random
number=random.randrange(0,100)
guess="wrong"
print("Welcome to Number Guessing game!")

while guess=="wrong":
	answer=int(input("Please input a number between 0 and 100:"))
	
	num=int(answer)
	if num<number:
		print("This is lower than the number.try again!")
	elif num>number:
		print("This is higher than the number.try again!")
	else:
		print("This is the correct number!youWon!")
		guess="correct"


