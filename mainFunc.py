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
#STARTS HERE
startLine()
