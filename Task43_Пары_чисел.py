'''
Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
'''
import math
from random import randint

def get_random_list() -> list:
    list_len = int(input("задай длину списка: "))
    lst = [randint(1, 10) for i in range(list_len)]
    return lst

random_list = get_random_list()
print(random_list)

mult_list = lambda random_list:[random_list[i] * random_list[-i-1] for i in range (math.ceil(len(random_list)/2))]
print(mult_list(random_list))