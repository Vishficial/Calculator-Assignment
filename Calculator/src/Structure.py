from src import Operators as O
from src import HandleErrors as H

def menu():
    print("1-Addition\n2-Substraction\n3-Multiplication\n4-Division\n5-power to\n6-Rounding\n7-Remaining\n00-Exit")

#executing Operations getting the input
def Eval():
    Vishi = True
    while Vishi is True:
#input for first value
        First = H.Num1()

#if the user wants to exit the app
        if First == 00:
            print("Closing the app")
            exit()


#input for second value
        Sec = H.Num2()

#if the user wants to end the app
        if Sec == 00:
            print("Closing the app")
            exit()


#input for the operator
        Oppe = H.Opp()



#Executing the Operations on input Values
        if Oppe == 1:
            print(O.add(First,Sec))
        elif Oppe ==2:
            print(O.sub(First,Sec))
        elif Oppe == 3:
            print(O.prod(First,Sec))
        elif Oppe == 4:
            print(O.div(First,Sec))
        elif Oppe == 5:
            print(O.exp(First,Sec))
        elif Oppe == 6:
            print(O.round(First,Sec))
        elif Oppe == 7:
            print(O.rem(First,Sec))
        elif Oppe == 00:
            print("Closing the app")
            Vishi = False



