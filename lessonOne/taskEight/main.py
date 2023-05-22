"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
    если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

n = int(input("Введите размер n: "))
m = int(input("Введите размер m: "))
k = int(input("Введите количество k: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("{} {} {} - yes".format(n, m, k))
else:
    print("{} {} {} - no".format(n, m, k))