def allocate_workload(total_workload, num_faculty):
    if num_faculty <= 0:
        print("Invalid number of faculty members.")
        return {}

    workload_per_faculty = total_workload / num_faculty

    allocations = {}
    for faculty_number in range(1, num_faculty + 1):
        faculty_name = input(f"Enter the name of Faculty {faculty_number}: ")
        allocations[faculty_name] = workload_per_faculty

    return allocations

def main():
    num_faculty = int(input("Enter the total number of faculty members: "))
    total_workload = float(input("Enter the total workload: "))

    allocations = allocate_workload(total_workload, num_faculty)

    print("\nAllocated workloads for faculty members:")
    for faculty, workload in allocations.items():
        print(f"{faculty}: {workload} hours")

if __name__ == "__main__":
    main()
