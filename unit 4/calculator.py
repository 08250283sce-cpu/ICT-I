a = float(input("enter a number:"))
b = float (input("enter a number:"))


def add(a,b):
    return(a+b)

def subtarct(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a, b):
    if b == 0:
        return " MA Error"
    return a / b

def show_menu():
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. Exit")

while True:
    show_menu()
    choice = input("What operation do you want to do? (1-5): ")

    

    if choice == "5":
        print("off")
        break


    elif choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtarct(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    
    else:
        print("Invalid choice! Please select between 1 and 5.")  


