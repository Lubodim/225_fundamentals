n = int(input("Въведете броя на учениците: "))
student_grades = {}

for _ in range(n):
    name, grade = input("Въведете име и оценка ").split()
    grade = float(grade)

    student_grades.setdefault(name, []).append(grade)

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f'{name} -> {formatted_grades} (avg: {avg_grade:.2f})')
