print("Welcome to my game")
name = input("What is your name? ")
# name = "j"
age = int(input("What is your age? "))
# age = 15
if age >= 18:
    print("Hello ",name, " you are " , age, " years old.")
else:
    print("Sorry, " ,name, " You can't play this game.")
    exit()
while True:
    hel = 10
    print("Let's Play this game")
    print("You are starting with", hel, "health.")
    c1 = input("First Choice..... Left or Right?" ).lower()


    if c1 == "right":
         l1 = input("You follow a path and reach at lake do you want to swim or go walk? ").lower()
        if l1 == "swim":
            print("You went around and reach the other side of lake.")
        elif l1 == "walk": 
            print("You bit by the fish and lost five heath.")
            hel -= 5



        print("You reach at home")


    elif c1 == "left":
        l1 = input("You follow a path and reach at lake do you want to swim or go walk? ").lower()
        if l1 == "swim":
            print("You went around and reach the other side of lake.")
        elif l1 == "walk": 
            print("You bit by the fish and lost five heath.")
            hel -= 5
        else:
            print("You fell down and lost")     


    
    else:
        print("You fell down and lost")


    i = input("Do you want to play this game again?(Yes/No)").lower()
    if i == "No":
        break

