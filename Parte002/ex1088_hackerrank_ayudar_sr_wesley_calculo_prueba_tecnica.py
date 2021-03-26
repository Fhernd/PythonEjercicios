# Ejercicio 1088: HackerRank Ayudar al sr. Wesley a caulcular los promedios de una prueba técnica.

# Task

# Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .

# Your task is to help Dr. Wesley calculate the average marks of the students.


# Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

# ...

from collections import namedtuple
import re

if __name__ == '__main__':
    n = int(input())
    
    columns = ','.join(input().split())
    

    Student = namedtuple('Student', columns)
    
    students = []
    
    for _ in range(n):
        data = input().split()
        students.append(Student(*data))
    
    marks = [int(getattr(s, 'MARKS')) for s in students]
    result = sum(marks) / len(marks)
    
    print('{:.2f}'.format(result))
