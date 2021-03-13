# Ejercicio 1044: HackerRank Buscar los estudiantes que tengan la segunda nota más baja.

# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta

# ....

def find_second_lowest_grade(students):
    grades = [s[1] for s in students]
    grades = sorted(grades)
    min_grade = grades[0]
    
    for i in range(len(grades)):
        if grades[i] > min_grade:
            return grades[i]
    
    return min_grade


def find_students_by_grade(students, grade):
    return [s[0] for s in students if s[1] == grade]


if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    
    second_lowest_grade = find_second_lowest_grade(students)
    students_by_grade = find_students_by_grade(students, second_lowest_grade)
    students_by_grade = sorted(students_by_grade)
    
    for s in students_by_grade:
        print(s)
