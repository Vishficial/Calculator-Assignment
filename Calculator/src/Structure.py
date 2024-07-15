from src import HandleErrors as H
from src import Operators as O


def menu():
    print("1-Addition\n2-Substraction\n3-Multiplication\n4-Division\n5-power to\n6-Rounding\n7-Remaining\n8-Show History\n0-Exit")

#executing Operations getting the input
def value():
    Vishi = True
    while Vishi is True:
            Oppe = H.Opp()
            if Oppe == 0:
                print("Closing the app")
                exit()
            # elif Oppe ==8:
            #     fh.show()

#input for first value

            First = H.Num1()


#input for second value
            Sec = H.Num2()



#Executing the Operations on input Values
            if Oppe == 1:
                Sum = O.add(First,Sec)
                print(f"{First}+{Sec}={Sum}")
            elif Oppe ==2:
                Sum = O.sub(First, Sec)
                print(f"{First}-{Sec}={Sum}")
            elif Oppe == 3:
                Sum = O.prod(First, Sec)
                print(f"{First}x{Sec}={Sum}")
            elif Oppe == 4:
                Sum = O.div(First, Sec)
                print(f"{First}/{Sec}={Sum}")
            elif Oppe == 5:
                Sum = O.exp(First, Sec)
                print(f"{First}^{Sec}={Sum}")
            elif Oppe == 6:
                Sum = O.round(First, Sec)
                print(f"{First}//{Sec}={Sum}")
            elif Oppe == 7:
                Sum = O.rem(First, Sec)
                print(f"{First}%{Sec}={Sum}")



