from src import ForHistory as fh
from src import Operators as O



#To get the integer value and preventing error if anyother value is entered


#Returns an integer value or prints "wrong input" for any other input

#For the first Number
def Num1():
    ash = True
    while ash is True:

        Entry = input("Enter the First Number:")
        try:
            First = int(Entry)
            ash = False
            return First

        except ValueError:
            print("Wrong input! Try Again")

#For the second Number
def Num2():
    ash = True
    while ash is True:

        Entry = input("Enter the Second Number:")
        try:
            Sec = int(Entry)
            # if Sec == 0:
            #     print("Cant Divide by Zero!")
            # else:
            ash = False
            return Sec

        except ValueError:
            print("wrong input! Try Again")

def Num3():
    ash = True
    while ash is True:
        Entry = input("Enter second number again!:")
        try:
            Sec2 = int(Entry)
            if Sec2 == 0:
                print("Cant divide by Zero!")
            else:
                ash = False
                return Sec2
        except ValueError:
            print("wrong input! Try Again")

#For the Operator
def Opp():
    Harry = True
    while Harry is True:

        Entry = input("Choose the Operator from Menu:")
        try:
            opp = int(Entry)

            if opp > 8:
                print("Try Again!")
            elif opp ==8:
                O.time_delay()
                fh.show()
            else:
                Harry = False
                return opp
        except ValueError:
            print("Wrong input! Try Again")

