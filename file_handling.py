# Writing to a file
with open("grades.txt", "w") as file:
    file.write("Student: Gowsziii\n")
    file.write("Grades: 90, 75, 22\n")
    file.write("Average: 62.3\n")
    file.write("Status: Passed\n") 

print("Data written to grades.txt")

# Reading from a file
with open("grades.txt", "r") as file:
    content = file.read()
    print("\nReading from file:")
    print(content)