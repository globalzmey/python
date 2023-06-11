"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5

"""

dim_size = int(input('Введите количество N элементов массива А: '))
dim_input = input('Введите через пробел элементы массива: ').split()
dim_nums = list(map(int, dim_input))
if len(dim_nums) != dim_size:
    print('Количество элементов не соответствуют заявленному!')
else:
    desired_num = int(input('Введите искомое число X: '))
    min = abs(desired_num - dim_nums[0])
    index = 0
    for i in range(dim_size):
        count = abs(desired_num - dim_nums[i])
        if count < min:
            min = count
            index = i
    print(f'Число {dim_nums[index]} в массиве A наиболее близко по величине к числу {desired_num}')