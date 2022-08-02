'''
Сформировать список из  N членов последовательности.
'''
import Function as f
n = int(f.is_int(input('введи число: ')))
print(n)

def get_sequence(n):
    return[ -3 **i for i in range (1, n+1)]
print(get_sequence(n))






