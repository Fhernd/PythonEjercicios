# Ejercicio 1070: HackerRank Encontrar los estudiantes suscritos a la versión en inglés de un diario.

# Task
# Students of District College have a subscription to English and French newspapers. Some students have subscribed
#  to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to
#  both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
# and one set has subscribed to the French newspaper. Your task is to find the total number of students 
# who have subscribed to only English newspapers.

# ...

if __name__ == '__main__':
    m = int(input())
    students_english = set(map(int, input().split()))
    
    n = int(input())
    students_french = set(map(int, input().split()))
    
    students_english_only = students_english - students_french
    print(len(students_english_only))
