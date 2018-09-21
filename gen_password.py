# Генератор паролей производной длины - только цифры
from random import randint
def f(x):
    return str(x)
p = list(map(f, range(1,randint(1,25))))
password = ''.join(p)
print(password)
