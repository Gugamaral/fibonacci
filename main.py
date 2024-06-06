import os
import math

f1 = 1
f2 = 1
f3 = 3 

def sequencia_fibonacci(fn):
    if f1 == 1:
        return 1
    if f2 == 1:
        return 1
    if f3 == 2:
        return 2
    else:
        return fn * sequencia_fibonacci('f1 - 1, + f2 - 2, f3 ≥ 3')


fn = int(input('Informe um número inteiro: '))

print(f'A sequencia de Fibonacci {fn}: é. ')