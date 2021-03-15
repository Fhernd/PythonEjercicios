# Ejercicio 1053: HackerRank Contar el número de ocurrencias de una subcadena en una cadena.

# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Constraints


# Each character in the string is an ascii character.

# ...

def count_substring(string, sub_string):
    counter = 0
    len_sub_string = len(sub_string)
    
    for i in range(len(string)):
        if string[i:i + len_sub_string] == sub_string:
            counter += 1
    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
