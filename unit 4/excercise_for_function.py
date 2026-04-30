
mark_1 = float(input("Enter mark1: "))
mark_2 = float(input("Enter mark2: "))
mark_3 = float(input("Enter mark3: "))

def calculate_marks(mark_1, mark_2, mark_3):
    return mark_1 + mark_2 + mark_3

def calculate_average(mark_1, mark_2, mark_3):
    return (mark_1 + mark_2 + mark_3) / 3

total = calculate_marks(mark_1, mark_2, mark_3)
average = calculate_average(mark_1, mark_2, mark_3)

print("The total for the 3 subjects is:", total)
print("The average for the 3 subjects is:", average)

if average >= 50:
    print("Pass")
else:
    print("Fail")



soanm = int(input("Enter a number: "))
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
    
print("The number is:", check_even_odd(soanm))
   
