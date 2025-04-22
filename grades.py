# Accept marks of three subjects
marks1 = input("Enter marks for Subject 1 (or type 'Absent'): ")
marks2 = input("Enter marks for Subject 2 (or type 'Absent'): ")
marks3 = input("Enter marks for Subject 3 (or type 'Absent'): ")

# Convert marks to integers if not absent
if marks1 != "Absent":
    marks1 = int(marks1)
if marks2 != "Absent":
    marks2 = int(marks2)
if marks3 != "Absent":
    marks3 = int(marks3)

# Determine grades for each subject
if marks1 == "Absent":
    grade1 = "NA"
elif 0 <= marks1 <= 39:
    grade1 = "F"
elif 40 <= marks1 <= 44:
    grade1 = "P"
elif 45 <= marks1 <= 49:
    grade1 = "C"
elif 50 <= marks1 <= 54:
    grade1 = "B"
elif 55 <= marks1 <= 59:
    grade1 = "B+"
elif 60 <= marks1 <= 69:
    grade1 = "A"
elif 70 <= marks1 <= 79:
    grade1 = "A+"
elif 80 <= marks1 <= 100:
    grade1 = "O"
else:
    grade1 = "Invalid Marks"

if marks2 == "Absent":
    grade2 = "NA"
elif 0 <= marks2 <= 39:
    grade2 = "F"
elif 40 <= marks2 <= 44:
    grade2 = "P"
elif 45 <= marks2 <= 49:
    grade2 = "C"
elif 50 <= marks2 <= 54:
    grade2 = "B"
elif 55 <= marks2 <= 59:
    grade2 = "B+"
elif 60 <= marks2 <= 69:
    grade2 = "A"
elif 70 <= marks2 <= 79:
    grade2 = "A+"
elif 80 <= marks2 <= 100:
    grade2 = "O"
else:
    grade2 = "Invalid Marks"

if marks3 == "Absent":
    grade3 = "NA"
elif 0 <= marks3 <= 39:
    grade3 = "F"
elif 40 <= marks3 <= 44:
    grade3 = "P"
elif 45 <= marks3 <= 49:
    grade3 = "C"
elif 50 <= marks3 <= 54:
    grade3 = "B"
elif 55 <= marks3 <= 59:
    grade3 = "B+"
elif 60 <= marks3 <= 69:
    grade3 = "A"
elif 70 <= marks3 <= 79:
    grade3 = "A+"
elif 80 <= marks3 <= 100:
    grade3 = "O"
else:
    grade3 = "Invalid Marks"

# Print subject-wise grades
print(f"Subject 1: {grade1}")
print(f"Subject 2: {grade2}")
print(f"Subject 3: {grade3}")

# Check if student has failed
if "F" in [grade1, grade2, grade3]:
    print("Result: Fail")
elif "NA" in [grade1, grade2, grade3]:
    print("Result: Incomplete (Absent in one or more subjects)")
else:
    # Calculate total and average
    total_marks = 0
    count = 0
    if marks1 != "Absent":
        total_marks += marks1
        count += 1
    if marks2 != "Absent":
        total_marks += marks2
        count += 1
    if marks3 != "Absent":
        total_marks += marks3
        count += 1

    average_marks = total_marks / count
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print("Result: Pass")

