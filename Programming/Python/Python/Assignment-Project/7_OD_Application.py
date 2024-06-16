od_applications = {}
faculty_approval = {'01'}

def apply_od():
    roll_no = input("Enter student roll number: ")
    name = input("Enter student name: ")
    attendance_percentage = float(input("Enter student attendance percentage: "))
    
    if attendance_percentage < 75:
        print("OD cannot be granted. Attendance is below 75%.")
        return

    reason = input("Enter reason for OD: ")

    if roll_no not in od_applications:
        od_applications[roll_no] = {
            "Name": name,
            "Attendance Percentage": attendance_percentage,
            "Reason for OD": reason,
            "Status": "Pending"
        }
        print(f"OD application for student {name} (Roll No: {roll_no}) has been submitted.")
    else:
        print(f"OD application for student {name} (Roll No: {roll_no}) already exists.")

def view_od_application(roll_no):
    if roll_no in od_applications:
        od_info = od_applications[roll_no]
        print(f"Roll No: {roll_no}")
        print(f"Name: {od_info['Name']}")
        print(f"Attendance Percentage: {od_info['Attendance Percentage']}%")
        print(f"Reason for OD: {od_info['Reason for OD']}")
        print(f"Status: {od_info['Status']}")
    else:
        print(f"No OD application found for Roll No: {roll_no}")

def faculty_action():
    faculty_id = input("Enter faculty ID: ")
    if faculty_id in faculty_approval:
        roll_no = input("Enter student roll number: ")
        if roll_no in od_applications:
            action = input("Approve (A) or Reject (R) the OD application: ").upper()
            if action == "A":
                od_applications[roll_no]["Status"] = "Approved"
                print("OD application approved.")
            elif action == "R":
                od_applications[roll_no]["Status"] = "Rejected"
                print("OD application rejected.")
            else:
                print("Invalid action. Please enter 'A' or 'R'.")
        else:
            print("Student not found.")
    else:
        print("Faculty not found.")

def exit_program():
    print("Exiting the program.")
    exit()

menu = {
    '1': apply_od,
    '2': view_od_application,
    '3': faculty_action,
    '4': exit_program,
}

def main():
    while True:
        print("\nOD Application System")
        print("1. Apply for OD")
        print("2. View OD Application")
        print("3. Faculty Action")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice in menu:
            menu[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
