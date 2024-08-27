import random

list_world=["India","America","Saudi","Dubai","Iran","Iraq","China"]

x=random.choice(list_world)
print("Choice Your country \n'India''America''Saudi''Dubai''Iran''Iraq''China'")

chance=int(input("How many chance you want"))

count=0

while count < chance:
	if chance > 10:
		print("You can Enter between 1-5")
		break

	print(f"You have a {chance} Chance")
	count+=1
	guess = input("Enter number for guess :- ")
	if guess == x:
		print("Congratulation you have choose Correct")
		break
	else:
		print("Try again")
	chance -= 1
if count >= chance:
	print(f"You have try {count} times")
