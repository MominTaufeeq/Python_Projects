import random

computer=random.choice([1,-1,0])
while True:
    nextchance = int(input("Enter 1 to Play Again and 2 for Exit"))
    if (nextchance == 1):
        user=input("Enter Your choice :")
        yourDict={"s":1,"w":-1,"g":0}
        reverstr={1:"Snake",-1 : "Water",0 :"Gun"}


        you=yourDict[user]
        print(f"You chose {reverstr[you]} \n Computer Chose {reverstr[computer]}")

        if computer == you:
            print("Draw")
        else:
            if(computer == -1 and you == 1):
                print("You Win")
            elif (computer == -1 and you == 0):
                print("You Lose")
            elif (computer == 1 and you == -1):
                print("You Lose")
            elif (computer == 1 and you == 0):
                print("You Win")
            elif (computer == 0 and you == -1):
                print("You Win")
            elif (computer == 0 and you == 1):
                print("You Lose")
            else:
                print("Something Went Wrong")
    else:
        break

