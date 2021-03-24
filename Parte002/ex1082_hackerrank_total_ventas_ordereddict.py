# Ejercicio 1082: HackerRank Obtener el total ventas de un supermercado con un objeto OrderedDict.

# Task

# You are the manager of a supermarket.
# You have a list of  items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

# ...

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    
    sales = OrderedDict()
    
    for _ in range(n):
        data = input().split()
        net_price = int(data[-1])
        item_name = ' '.join(data[:len(data) - 1])
        
        if item_name in sales:
            sales[item_name].append(net_price)
        else:
            sales[item_name] = [net_price]
    
    for k, v in sales.items():
        print(k, sum(v))
