# Ejercicio 1043: HackerRank Encontrar el segundo puntaje mayor en una competición de deportes.

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# ...

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = sorted(list(arr))
    
    maximum = scores[-1]
    runner_up = maximum
    
    for i in range(len(scores) - 1, -1, -1):
        if scores[i] < maximum:
            runner_up = scores[i]
            break
    
    print(runner_up)

