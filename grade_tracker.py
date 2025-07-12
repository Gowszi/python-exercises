# 1. Student dictionary
student = {
    "name": "Gowsziii",
    "grades": [90, 75, 22]
}

# 2. Function to calculate average
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

# 3. Use the function and print results
average = calculate_average(student["grades"])
print("Student:", student["name"])
print("Grades:", student["grades"])
print("Average:", average)

# Check if passed or failed
if average >= 50:
    print("Passed")
else:
    print("Failed")

# 4. Add a new grade
student["grades"].append(88)
print("New grades:", student["grades"])

# 5. Remove the lowest grade
student["grades"].remove(min(student["grades"]))
print("After removing lowest grade:", student["grades"])
