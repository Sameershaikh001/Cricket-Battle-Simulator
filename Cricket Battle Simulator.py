# Cricket game using random function 
import random as rd
def fun1():
    temp = 1
    score1 = 0
    ball1=0
    while temp == 1:
        user_bat = int(input("Your batting!\nEnter between (0,6): "))
        computer_def = rd.randint(0, 6)
        if user_bat > -1 and user_bat <= 6:
            ball1+=1
            if user_bat == computer_def:
                score1 += user_bat + computer_def
                print(f"Number Provided by computer is {computer_def}")
                print(f"Out! Your final score is {score1}/{ball1}\n\n")
                temp = 2
                return score1,ball1
                break
            else:
                score1 += user_bat + computer_def
                print(f"Number Provided by computer is {computer_def}")
                print(f"Your score till now {score1}/{ball1}\n")
        else:
            print("Wrong input! It should be between (0,6)")

def fun2():
    temp = 1
    score2 = 0
    ball2=0
    while temp == 1:
        user_bat = int(input("Your bowling!\nEnter between (0,6): "))
        computer_def = rd.randint(0, 6)
        if user_bat > -1 and user_bat <= 6:
            ball2+=1
            if user_bat == computer_def:
                score2 += user_bat + computer_def
                print(f"Number Provided by computer is {computer_def}")
                print(f"Out! Computer's final score is {score2}/{ball2}\n\n")
                temp = 2
                return score2, ball2                
                break
            else:
                score2 += user_bat + computer_def
                print(f"Number Provided by computer is {computer_def}")
                print(f"Computer's score till now {score2}/{ball2}\n")
        else:
            print("Wrong input! It should be between (0,6)")

def fun3():
        if score1 > score2:
            print(f"You won!\nYour score: {score1}/{ball1}\nComputer score: {score2}/{ball2}")
        elif score1 < score2:
            print(f"Computer won!\nComputer score: {score2}/{ball2}\nYour score: {score1}/{ball1}")
        else:
            print(f"Draw!\nYour score: {score1}/{ball1}\nComputer score: {score2}/{ball2}")
             
var1 = input("Coin is flipping....enter choice between (H,T): ").upper()
var2 = rd.choice(["H","T"])

if (var1=="H"or var1=="T"):
    if var1 == var2:
        print("Won the Toss! Go for batting\n")
        score1,ball1 = fun1()
        score2,ball2 = fun2()
        result1= fun3()
    else:
        print("Loss the Toss! Go for bowling\n")
        score2,ball2 = fun2()
        score1,ball1 = fun1()
        result2= fun3()
else:
    print("Wrong input! It should be H or T")
