for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum([i * 10 ** j for j in range(i)]))
