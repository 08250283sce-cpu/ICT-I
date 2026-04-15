no_of_student = int(input("Enter the number of students:"))
i= 1
students_name = {}
while i <= no_of_student:
    name = input("Enter the name of the students:")
    print("The name of students {} is {}".format(i,name))
    i+=1
    students_name[i]= name

print(students_name)