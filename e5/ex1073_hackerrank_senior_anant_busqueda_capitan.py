# Ejercicio 1073: HackerRank Ayudar al señor Anant a encontrar al capitán en un grupo de turistas.

# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of  members per group where  ≠ .

# ...

from collections import Counter

if __name__ == '__main__':
    k = int(input())
    
    rooms = list(map(int, input().split()))
    
    count = Counter(rooms)
    result = count.most_common()[-1][0]
    print(result)
