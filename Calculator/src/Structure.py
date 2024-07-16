from src import HandleErrors as H
from src import Operators as O



def menu():
     print("!Choose from following!\n1-Addition\n2-Substraction\n3-Multiplication\n4-Division\n5-power to\n6-Rounding\n7-Remaining\n8-Show History\n0-Exit\n!VISHFICIAL!")



#executing Operations getting the input
def value():
    Vishi = True
    while Vishi is True:
            Oppe = H.Opp()
            if Oppe == 0:
                print("Closing the app")
                exit()

#input for first value

            First = H.Num1()


#input for second value
            Sec = H.Num2()




#Executing the Operations on input Values
            if Sec == 0 and Oppe == 4:
                print("Cant divide by two!")
                Sec2 = H.Num3()
                Total = O.div(First,Sec2)
                O.time_delay()
                print(f"{First}/{Sec2}={Total}")
            elif Sec == 0 and Oppe == 6:
                print("Cant divide by two!")
                Sec2 = H.Num3()
                Total = O.round(First,Sec2)
                print(f"{First}//{Sec2}={Total}")
            elif Sec == 0 and Oppe == 7:
                print("Cant divide by two!")
                Sec2 = H.Num3()
                Total = O.rem(First, Sec2)
                print(f"{First}%{Sec2}={Total}")

            elif Oppe == 1:
                Sum = O.add(First,Sec)
                O.time_delay()
                print(f"{First}+{Sec}={Sum}")
            elif Oppe ==2:
                Sum = O.sub(First, Sec)
                O.time_delay()
                print(f"{First}-{Sec}={Sum}")
            elif Oppe == 3:
                Sum = O.prod(First, Sec)
                O.time_delay()
                print(f"{First}x{Sec}={Sum}")
            elif Oppe == 4:
                Sum = O.div(First, Sec)
                O.time_delay()
                print(f"{First}/{Sec}={Sum}")
            elif Oppe == 5:
                Sum = O.exp(First, Sec)
                O.time_delay()
                print(f"{First}^{Sec}={Sum}")
            elif Oppe == 6:
                Sum = O.round(First, Sec)
                O.time_delay()
                print(f"{First}//{Sec}={Sum}")
            elif Oppe == 7:
                Sum = O.rem(First, Sec)
                O.time_delay()
                print(f"{First}%{Sec}={Sum}")



