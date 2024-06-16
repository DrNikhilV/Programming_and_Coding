student_records = {}

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    date_of_birth = input("Enter student date of birth (YYYY-MM-DD): ")
    twelfth_percentage = input("Enter student 12th percentage: ")
    mobile_no = input("Enter student mobile number: ")
    email_id = input("Enter student email ID: ")

    student_records[student_id] = {
        "Name": name,
        "Age": age,
        "Date of Birth": date_of_birth,
        "12th Percentage": twelfth_percentage,
        "Mobile Number": mobile_no,
        "Email ID": email_id
    }
    
    print(f"Student with ID {student_id} has been enrolled.")

def view_student(student_id):
    if student_id in student_records:
        student_info = student_records[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student_info['Name']}")
        print(f"Age: {student_info['Age']}")
        print(f"Date of Birth: {student_info['Date of Birth']}")
        print(f"12th Percentage: {student_info['12th Percentage']}")
        print(f"Mobile Number: {student_info['Mobile Number']}")
        print(f"Email ID: {student_info['Email ID']}")
    else:
        print(f"Student with ID {student_id} does not exist.")

def remove_student(student_id):
    if student_id in student_records:
        del student_records[student_id]
        print(f"Student with ID {student_id} has been removed.")
    else:
        print(f"Student with ID {student_id} does not exist.")

def main():
    while True:
        print("\nStudent Enrollment System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Remove Student")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            student_id = input("Enter student ID: ")
            view_student(student_id)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            remove_student(student_id)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
