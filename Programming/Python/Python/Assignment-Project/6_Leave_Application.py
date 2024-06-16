leave_applications = {}

def apply_leave():
    roll_no = input("Enter student roll number: ")
    name = input("Enter student name: ")
    attendance_percentage = float(input("Enter student attendance percentage: "))
    
    if attendance_percentage < 75:
        print("Leave cannot be granted. Attendance is below 75%.")
        return

    reason = input("Enter reason for leave: ")

    if roll_no not in leave_applications:
        leave_applications[roll_no] = {
            "Name": name,
            "Attendance Percentage": attendance_percentage,
            "Reason for Leave": reason
        }
        print(f"Leave application for student {name} (Roll No: {roll_no}) has been submitted.")
    else:
        print(f"Leave application for student {name} (Roll No: {roll_no}) already exists.")

def view_leave_application(roll_no):
    if roll_no in leave_applications:
        leave_info = leave_applications[roll_no]
        print(f"Roll No: {roll_no}")
        print(f"Name: {leave_info['Name']}")
        print(f"Attendance Percentage: {leave_info['Attendance Percentage']}%")
        print(f"Reason for Leave: {leave_info['Reason for Leave']}")
    else:
        print(f"No leave application found for Roll No: {roll_no}")

def main():
    while True:
        print("\nLeave Application System")
        print("1. Apply for Leave")
        print("2. View Leave Application")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            apply_leave()
        elif choice == '2':
            roll_no = input("Enter student roll number: ")
            view_leave_application(roll_no)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
