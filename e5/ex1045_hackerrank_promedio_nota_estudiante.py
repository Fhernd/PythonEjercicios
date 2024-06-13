# Ejercicio 1045: HackerRank Calcular el promedio de 3 notas de un estudiante en un conjunto de datos.

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example




# The query_name is 'beta'. beta's average score is .

# Input Format

# The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

# ...

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = sum(student_marks[query_name])/3
    
    print('{:.2f}'.format(average))

