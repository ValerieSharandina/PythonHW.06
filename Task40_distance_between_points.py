'''
Найти расстояние между двумя точками пространства(числа вводятся через пробел)
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

import math
a = list(map(int, input('Введи числа: ').split()))
res = round(math.sqrt((a[2]-a[0])**2+(a[3]-a[1])**2), 2)
print(res)

