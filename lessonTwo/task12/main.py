"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
x, y = map(int, input('Введите через пробел сумму чисел X Y, затем их произведение: ').split())
for i in range(1, min(x, y) + 1):
        for j in range(1, min(x, y) + 1):
            if i + j == x and i * j == y:
                ansq = i
                answ = j

print("Загаданные числа X Y: {} {}".format(str(min(ansq, answ)), str(max(ansq, answ))))