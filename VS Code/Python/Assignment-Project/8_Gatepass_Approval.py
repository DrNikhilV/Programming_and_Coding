gatepass_requests = {}
faculty_approval = {'01'}

def request_gatepass():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    reason = input("Enter reason for gatepass: ")

    if student_id not in gatepass_requests:
        gatepass_requests[student_id] = {
            "Name": name,
            "Reason": reason,
            "Status": "Pending"
        }
        print(f"Gatepass request for student {name} (ID: {student_id}) has been submitted.")
    else:
        print(f"Gatepass request for student {name} (ID: {student_id}) already exists.")

def view_gatepass_request(student_id):
    if student_id in gatepass_requests:
        request_info = gatepass_requests[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {request_info['Name']}")
        print(f"Reason for Gatepass: {request_info['Reason']}")
        print(f"Status: {request_info['Status']}")
    else:
        print(f"No gatepass request found for Student ID: {student_id}")

def faculty_action():
    faculty_id = input("Enter faculty ID: ")
    if faculty_id in faculty_approval:
        student_id = input("Enter student ID: ")
        if student_id in gatepass_requests:
            action = input("Approve (A) or Reject (R) the gatepass request: ").upper()
            if action == "A":
                gatepass_requests[student_id]["Status"] = "Approved"
                print("Gatepass request approved.")
            elif action == "R":
                gatepass_requests[student_id]["Status"] = "Rejected"
                print("Gatepass request rejected.")
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
    '1': request_gatepass,
    '2': view_gatepass_request,
    '3': faculty_action,
    '4': exit_program,
}

def main():
    while True:
        print("\nGatepass Approval System")
        print("1. Request Gatepass")
        print("2. View Gatepass Request")
        print("3. Faculty Action")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice in menu:
            menu[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
