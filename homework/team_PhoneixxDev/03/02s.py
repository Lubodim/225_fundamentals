n = int(input("Enter the number of students: "))

students = {}

for _ in range(n):
    name, grade = input("Enter student name and grade: ").split()
    grade = float(grade)

    if name in students:
        student_info = students[name]
        updated_student_info = (student_info[0] + (grade,), student_info[1] + 1)
        students[name] = updated_student_info
    else:
        students[name] = (grade,), 1

for student, (grades, count) in students.items():
    avg_grade = sum(grades) / count
    formatted_grades = ' '.join(map(str, grades))
    print(f"{student} -> {formatted_grades} (avg: {avg_grade:.2f})")
