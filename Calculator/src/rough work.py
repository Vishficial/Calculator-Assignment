import time
def add_file(entry):
    file = open("History.txt", "a")
    file.write(entry + "\n" )

# def add(a,b):
#     sum = a+b
#     entry = f"{a} + {b} = {sum}"
#     add_file(entry)
#     return entry
# F = int(input("enter first number:"))
# S = int(input("enter second number:"))
# T = add(F,S)
# print(".",end="")
# time.sleep(1)
# print(".",end="")
# time.sleep(1)
# print(".",end="")
# time.sleep(1)
# print(".")
# print(T)



