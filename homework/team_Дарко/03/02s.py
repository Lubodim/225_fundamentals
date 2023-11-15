n = int(input())

students_data = {}

for i in range(n):
    student_data = input()
    name, grade = student_data.split()
    grade = float(grade)

    if name in students_data:
        students_data[name].append(grade)
    else:
        students_data[name] = [grade]

average_grades = {}
for name, grades in students_data.items():
    average_grade = sum(grades) / len(grades)
    average_grades[name] = average_grade

for name, grades in students_data.items():
    average_grade = average_grades[name]
    print(f"{name} -> {', '.join(map(str, grades))} (avg: {average_grade:.2f})")
