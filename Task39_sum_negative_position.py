'''
Найти сумму чисел списка стоящих на нечетной позиции
'''

import Function as f


nums = list(range(1, int(f.is_int(input('введи число: ')))+1))

print(f"{nums} -> {sum([elem[1] for elem in (filter(lambda x: x[0]%2 != 0, enumerate(nums)))])}")




