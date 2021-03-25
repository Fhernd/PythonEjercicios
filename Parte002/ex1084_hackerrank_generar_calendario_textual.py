# Ejercicio 1084: HackerRank Generar un calendario en formato texto con el módulo calendar.

# Task

# You are given a date. Your task is to find what the day is on that date.

# Input Format

# A single line of input containing the space separated month, day and year, respectively, in    format.

# ...

import calendar

if __name__ == '__main__':
    month, day, year = tuple(map(int, input().split()))
    
    result = calendar.weekday(year, month, day)
    
    result = list(calendar.day_name)[result].upper()
    
    print(result)
