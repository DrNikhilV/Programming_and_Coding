def create_timetable():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = {
        1: '9:00 AM - 10:00 AM',
        2: '10:00 AM - 11:00 AM',
        3: '11:00 AM - 12:00 PM',
        4: '1:00 PM - 2:00 PM',
        5: '2:00 PM - 3:00 PM'
    }
    subjects = {
        1: 'OS',
        2: 'DS',
        3: 'Python',
        4: 'Maths',
        5: 'AI',
        6: 'Biology',
        7: 'ICN',
        8: 'Lifeskills'
    }
    timetable = {day: {slot: None for slot in time_slots.values()} for day in days}

    return days, time_slots, subjects, timetable

def add_class(timetable, day, slot, subject):
    timetable[day][slot] = subject

def display_timetable(timetable, days, time_slots):
    for day in days:
        print(f"{day}:")
        for slot, subject in timetable[day].items():
            print(f"  {slot}: {subject}")

def main():
    days, time_slots, subjects, timetable = create_timetable()

    for day in days:
        print(f"Select 5 subjects for {day} by entering the subject number:")
        selected_subjects = []
        for _ in range(5):
            print(f"Available subjects: {', '.join([f'{num}: {subj}' for num, subj in subjects.items() if subj not in selected_subjects])}")
            subject_num = int(input("Enter subject number: "))
            while subject_num not in subjects or subjects[subject_num] in selected_subjects:
                print("Invalid subject number or subject already selected. Try again.")
                subject_num = int(input("Enter subject number: "))
            selected_subjects.append(subjects[subject_num])

            print(f"Available time slots: {', '.join([f'{num}: {slot}' for num, slot in time_slots.items() if timetable[day][slot] is None])}")
            slot_num = int(input("Enter time slot number: "))
            while slot_num not in time_slots or timetable[day][time_slots[slot_num]] is not None:
                print("Invalid time slot number or slot already occupied. Try again.")
                slot_num = int(input("Enter time slot number: "))
            add_class(timetable, day, time_slots[slot_num], subjects[subject_num])

    display_timetable(timetable, days, time_slots)

if __name__ == "__main__":
    main()
