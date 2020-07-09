chbt = {"what is your name": "I'm Bot","how old are you": "1 Day","where do you live":"I'm Everywhere","what does you do":"Nothing"}
print("\t\tWELCOME\n")
while True:
    a=input("Enter your Question: ")
    b=a.lower()
    print(chbt[b])
    i = input("If you want to ask more Questions Enter Y: ")
    if(i!='y' and i!='Y'):
        break
print("Thank You!")