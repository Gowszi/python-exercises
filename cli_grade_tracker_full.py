import json
import os

DATA_FILE = "students_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_student_name():
    while True:
        name = input("Enter student's name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")

def get_grades():
    grades = []
    while True:
        try:
            count = int(input("How many grades do you want to enter? "))
            if count > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a number.")

    for i in range(count):
        while True:
            try:
                grade = int(input(f"Enter grade {i+1}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")
    return grades

def calculate_average(grades):
    return sum(grades) / len(grades)

def add_student(data):
    name = get_student_name()
    grades = get_grades()
    average = calculate_average(grades)
    status = "Passed" if average >= 50 else "Failed"

    student = {
        "name": name,
        "grades": grades,
        "average": average,
        "status": status
    }
    data.append(student)
    save_data(data)
    print(f"\n✅ Student {name} added with average {average:.2f} ({status})")

def view_students(data):
    if not data:
        print("\nNo students found.")
        return
    print("\nSaved Students:")
    for i, student in enumerate(data, start=1):
        print(f"{i}. {student['name']} - Grades: {student['grades']}, Average: {student['average']:.2f}, Status: {student['status']}")

def main():
    data = load_data()
    while True:
        print("\n--- CLI Grade Tracker Menu ---")
        print("1. Add new student")
        print("2. View all students")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()
