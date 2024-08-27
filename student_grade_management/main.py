student={}
print("Welcome to the Student Grade Management System")
while True:
    print("1 for Adding\n2 for Update\n3 for Delete\n4 for View\n5 for exit")
    user=int(input("Enter your Choice :-"))
    if user == 1:
        student_name=input("Enter student Name :-")
        student_marks=int(input("Enter your Marks:- "))
        student[student_name]=student_marks
        print(f"Added Successfully is {student_name} ")
    elif user == 2:
        student_name1=input("Enter the name of student you want to update:-")
        if student_name1 in student:
            new_student=input("Enter value to update :-")
            student[student_name1] = new_student
            print("Your Given Value is updated Successfullt")
    elif user == 3:
        student_name1=input("Enter the name of student you want to delete :-")
        if student_name1 in student:
            del student[student_name1]
            print("Student Is Deleted Successfully")
    elif user == 4:
            print(student)
    elif user == 5:
        print("Closing your Program")
        break
    else:
        print("Invalid Value")
    # print(student)