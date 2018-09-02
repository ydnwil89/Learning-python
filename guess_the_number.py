import random

pc_num = random.randint(1,10)
user_num = 0
lifes = 3

while lifes != 0:
    user_num = int(input("Enter your number"))
    
    if user_num > pc_num: 
        print("Your number must be lower")
        lifes = lifes - 1
        print("You have only " + str(lifes) + " " + "lifes")

    elif user_num < pc_num:
         print("Your number must be higher")
         lifes = lifes - 1
         print("You have only " + str(lifes) + " " + "lifes")
    else:
         print("You are right! It was " + str(pc_num))
         print("Your lifes: " + str(lifes))


         break

if lifes == 0:
    print("You loose")
