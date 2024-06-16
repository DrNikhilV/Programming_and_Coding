def allocate_classrooms(num_classes, class_sizes, classroom_names):
    if num_classes > len(classroom_names):
        print("Not enough classrooms available for each class.")
        return

    allocations = {}
    used_classrooms = []

    for class_name, size in class_sizes.items():
        allocated = False
        for classroom in classroom_names:
            if classroom not in used_classrooms:
                allocations[classroom] = class_name
                used_classrooms.append(classroom)
                allocated = True
                break
        if not allocated:
            print(f"No available classroom for {class_name}")

    return allocations

def main():
    num_classes = int(input("Enter the number of classes: "))
    class_sizes = {}

    for i in range(1, num_classes + 1):
        class_name = input(f"Enter the name of Class {i}: ")
        num_students = int(input(f"Enter the number of students in Class {i}: "))
        class_sizes[class_name] = num_students

    classroom_names = [
        "Classroom 1", "Classroom 2", "Classroom 3", "Classroom 4",
        "Classroom 5", "Classroom 6", "Classroom 7", "Classroom 8"
    ]

    allocations = allocate_classrooms(num_classes, class_sizes, classroom_names)

    print("\nClassroom Allocations:")
    for classroom, allocated_class in allocations.items():
        print(f"{classroom}: {allocated_class}")

if __name__ == "__main__":
    main()
