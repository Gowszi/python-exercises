while True:
    # Get student's name
    name = input("Enter student's name: ")

    grades = []
    for i in range(3):
        while True:
            try:
                grade = int(input(f"Enter grade {i+1}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break  # valid input, exit inner loop
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = sum(grades) / len(grades)
    status = "Passed" if average >= 50 else "Failed"

    filename = f"{name.lower().replace(' ', '_')}_grades.txt"

    with open(filename, "w") as file:
        file.write(f"Student: {name}\n")
        file.write(f"Grades: {grades}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Status: {status}\n")

    print(f"\n✅ Grade data saved to {filename}")

    with open(filename, "r") as file:
        print("\n📄 Saved File Content:")
        print(file.read())

    # Ask if user wants to continue
    cont = input("Add another student? (y/n): ").lower()
    if cont != "y":
        print("Goodbye!")
        break  # Exit the while loop
