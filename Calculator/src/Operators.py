from src import ForHistory as Hi

#Function for addition fo two input values
def add(num1, num2):
    Sum = num1+num2
    entry= f"{num1}+{num2}={Sum}"
    Hi.add_file(entry)
    return Sum


#Function for substraction for two input values
def sub(num1, num2):
    Sum = num1-num2
    entry = f"{num1}-{num2}={Sum}"
    Hi.add_file(entry)
    return Sum

#Function for multiplication for two input values
def prod(num1, num2):
    Sum = num1 * num2
    entry = f"{num1}x{num2}={Sum}"
    Hi.add_file(entry)
    return Sum

#Function for division without remainder
def div(num1, num2):
    Sum = num1 / num2
    entry = f"{num1}/{num2}={Sum}"
    Hi.add_file(entry)
    return Sum

#Function for the rounded answer
def round(num1, num2):
    Sum = num1 // num2
    entry = f"{num1}//{num2}={Sum}"
    Hi.add_file(entry)
    return Sum


#Function for remainder
def rem(num1, num2):
    Sum = num1 % num2
    entry = f"{num1}%{num2}={Sum}"
    Hi.add_file(entry)
    return Sum


#Function for the exponential
def exp(num1, num2):
    Sum = num1 ** num2
    entry = f"{num1}^{num2}={Sum}"
    Hi.add_file(entry)
    return Sum

# F = int(input("enter no.:"))
# S = int(input("enter no.:"))
# Sum = add(F,S)
# print(Sum)

