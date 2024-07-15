
#Records the calculations done by the user
def add_file(entry):
    file = open('History.txt', "a")
    file.write(entry + "\n")

#shows the history upon command

def show():
    file = open('History.txt', "r")
    history = file.readlines()
    try:
        if history:
            print("History:")
            for line in history:
                print(line.strip())
        else:
            print("No History Found!")
    except Exception as e:
        print(f"an error occured while reading history:{e}")


