# Ejercicio 1071: HackerRank Estudiantes únicamennte suscritos a la edición en inlgés y francés de un diario.

# Task
# Students of District College have subscriptions to English and French newspapers. Some students have subscribed
#  to English only, some have subscribed to French only, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set 
# has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed 
# to either the English or the French newspaper but not both.

# ...

if __name__ == '__main__':
    m = int(input())
    english_students = set(map(int, input().split()))
    
    n = int(input())
    french_students = set(map(int, input().split()))
    
    s = english_students.symmetric_difference(french_students)
    
    print(len(s))
