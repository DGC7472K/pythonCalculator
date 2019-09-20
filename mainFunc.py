import time

#Introduction function
def startLine():
    polar = input("Use calculator function? (input polar value)\n")
    polarY = ["yes","y","yeah","ye","yess", "yee","yea","yesss"]
    polarN = ["no","n","nah","nope"]
    if polar.lower() in polarY:
        print("Ok\n")
        equation1()
    elif polar.lower() in polarN:
        print("Ok, good bye!\n")
    else:
        print("Invalid response\nTry again..")
        startLine()

#calculator function
def equation1():
    num1 = float(input("Input a numeric value:\n"))
    acceptNum = [0,1,2,3,4,5,6,7,8,9]
    if num1 in acceptNum:
        num2 = float(input("Input a numeric value:\n"))
        if num2 in acceptNum:
            op = str(input("Input an operator:\n"))
            acceptOp = ["+","-","/","x","*"]
            if op in acceptOp:
                if op == "+":
                    print("The answer to "+ str(round(num1)) + " + " + str(round(num2)) + " is: ")
                    print(round(num1+num2))
                    input("")
                    startLine()
                elif op == "-":
                    print("The answer to "+ str(round(num1)) + " - " + str(round(num2)) + " is: ")
                    print(round(num1-num2))
                    input("")
                    startLine()
                elif op == "/":
                    print("The answer to "+ str(round(num1)) + " / " + str(round(num2)) + " is: ")
                    print(round(num1/num2))
                    input("")
                    startLine()
                elif op == "x" or "X" or "*":
                    print("The answer to "+ str(round(num1)) + " x " + str(round(num2)) + " is: ")
                    print(round(num1*num2))
                    input("")
                    startLine()
            else:
                print("Invalid operator")
                equation1()
        else:
            print("Invalid input")
            equation1()
    else:
        print("Invalid input")
        equation1()

#Home screen function
def welcome():
    print("Greetings!")
    proceed = input("Press any key to continue..")
    intro()
    
#Log in function
def terminal():
    password = 2019
    tries = 0
    count = 0
    limit = 3
    retry = False
    lockout = False
    while password != tries and not lockout:
        if count < limit:
            tries = int(input("Password: "))
            if len(str(tries))<=4 and len(str(tries))>=4:
                count = count + 1
            else:
                print("Incorrect number of digits entered")
        else:
              lockout = True
    if lockout == True:
        print("Three incorrect answers..")
        time.sleep(2)
        print("You have been locked out")
    else:
        print("Correct password")
        print("Loading, please wait...")
        time.sleep(5)
        print("Hello!")
        
#Intro function        
def intro():
    polar = input("Login? ")
    polarY = ["yes","y","yeah","ye","yess", "yee","yea","yesss"]
    polarN = ["no","n","nah","nope"]
    if polar.lower() in polarY:
        print("You have 3 attempts")
        terminal()
    elif polar.lower() in polarN:
        print("Ok, good bye!\n")
        time.sleep(3)
        welcome()
    else:
        print("Invalid response\nTry again..")
        intro()
welcome()
startLine()
