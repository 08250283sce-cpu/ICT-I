detail = open("student.txt", "w")
detail.write("Sonam Choki:10203005682\n")
detail.write("Sangay Chhoden:10203003284\n")
detail.write("Dawa:1208000879\n")
detail.write("Sonam Zam:10203004569\n")
detail.write("Zhaoyiran:10203005678\n")
detail.close()

print("Dummy file 'student.txt' created successfully!")


with open("student.txt", "r") as f:
    students = f.readlines()
search_name = input("Enter student name to search: ")

found = False
for line in students:
    if search_name.lower() in line.lower():  
        print("Student found")
        found = True
        break

if not found:
    print("Student not found in the file.")
