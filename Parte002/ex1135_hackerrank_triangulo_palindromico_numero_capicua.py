for i in range(1, int(input()) + 1):
    print(sum(list(map(lambda x: 10 ** x, range(i)))) ** 2)
