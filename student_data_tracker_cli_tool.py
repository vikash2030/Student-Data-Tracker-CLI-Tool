import csv


def get_student_details():
    """
    Prompts user to input student details and returns a dictionary.
    Validates inputs with exception handling.

    Returns:
        dict: Student details including name, roll number and list of marks.
        None: If input validation fails.
    """
    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        roll_number = input("Enter roll number: ").strip()
        if not roll_number:
            raise ValueError("Roll number cannot be empty.")

        marks = []
        for i in range(1, 4):
            mark_input = input(f"Enter marks for subject {i} (0-100): ").strip()
            mark = float(mark_input)
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")
            marks.append(mark)

        return {"name": name, "roll_number": roll_number, "marks": marks}

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None


def display_records(records):
    """
    Displays all student records in a formatted table.

    Args:
        records (list): List of student record dictionaries.
    """
    if not records:
        print("No records to display.")
        return

    print("\nStudent Records:")
    print("-" * 60)
    print(f"{'Name':<20} {'Roll No.':<10} {'Marks (3 Subjects)':<25}")
    print("-" * 60)
    for rec in records:
        marks_str = ", ".join(f"{m:.1f}" for m in rec['marks'])
        print(f"{rec['name']:<20} {rec['roll_number']:<10} {marks_str:<25}")
    print("-" * 60)


def calculate_average(records):
    """
    Calculates and displays the average marks for each student.

    Args:
        records (list): List of student record dictionaries.
    """
    if not records:
        print("No records to calculate averages.")
        return

    print("\nAverage Marks per Student:")
    print("-" * 40)
    print(f"{'Name':<20} {'Average Marks':<15}")
    print("-" * 40)
    for rec in records:
        avg = sum(rec['marks']) / len(rec['marks'])
        print(f"{rec['name']:<20} {avg:.2f}")
    print("-" * 40)


def save_to_csv(records, filename="student_records.csv"):
    """
    Saves student records to a CSV file.

    Args:
        records (list): List of student record dictionaries.
        filename (str): Output CSV filename.
    """
    try:
        with open(filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header row
            writer.writerow(["Name", "Roll Number", "Subject 1", "Subject 2", "Subject 3"])
            # Write student data rows
            for rec in records:
                row = [rec['name'], rec['roll_number']] + rec['marks']
                writer.writerow(row)
        print(f"Records saved successfully to '{filename}'.")
    except IOError as e:
        print(f"Failed to save records: {e}")


def main():
    """
    Main function to run the command-line interface for student record management.
    """
    records = []

    while True:
        print("\n--- Student Records Manager ---")
        print("1. Add student record")
        print("2. Display all records")
        print("3. Calculate average marks")
        print("4. Save records to CSV")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            student = get_student_details()
            if student:
                records.append(student)
                print("Student record added successfully.")
        elif choice == '2':
            display_records(records)
        elif choice == '3':
            calculate_average(records)
        elif choice == '4':
            save_to_csv(records)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
