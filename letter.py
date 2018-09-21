user = input("Введите букву: ")
lst = ['самовар','весна','лето']

import random

i = random.randint(0,(len(lst)-1))
word = lst[i]
print('Случайное слово: ',lst[i])

j = random.randint(0,(len(list(word))-1))
letter = list(word)[j]
print('Случайная буква: ',letter)

if user == letter:
    print("Вы угадали!")
else:
    print("Попробуй еще раз!")
