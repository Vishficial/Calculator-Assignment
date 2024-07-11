from src import Operators as O

def menu():
    print("1-Addition\n2-Substraction\n3-Multiplication\n4-Division\n5-power to\n6-Rounding\n7-Remaining\n00-Exit")

#executing Operations getting the input
def Eval():
    Vishi = True
    while Vishi is True:
#input for first value
        First = int(input("::"))

        #if the user wants to exit the app
        if First == 00:
            print("Closing the app")
            exit()
#input for second value
        Sec = int(input("::"))

        #if the user wants to end the app
        if Sec == 00:
            print("Closing the app")
            exit()
#input for the operator
        Opp = int(input("**"))

        if Opp == 1:
            print(O.add(First,Sec))
        elif Opp ==2:
            print(O.sub(First,Sec))
        elif Opp == 3:
            print(O.prod(First,Sec))
        elif Opp == 4:
            print(O.div(First,Sec))
        elif Opp == 5:
            print(O.exp(First,Sec))
        elif Opp == 6:
            print(O.round(First,Sec))
        elif Opp == 7:
            print(O.rem(First,Sec))
        elif Opp == 00:
            print("Closing the app")
            Vishi = False
        else:
            print("Wrong Input,Try Again")


