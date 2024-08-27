import random
import math

lower=int(input("Enter the Lower number :- "))
upper=int(input("Enter the Upper Number :- "))

x=random.randint(lower,upper)

print(f"You have a {round(math.log(upper-lower+1,3))} Chance")

count=0
while count < math.log(upper-lower+1,3):
	count+=1
	guess = int(input("Enter number for guess :- "))
	if guess == x:
		print("Congratulation you have choose Correct")

	elif guess > x:
		print("You have choose to high")
	elif guess < x:
		print("You have choose to small")
if count >= math.log(upper-lower+1,2):
	print("Better Luck Next time")
	print(f"You have try {count} times")