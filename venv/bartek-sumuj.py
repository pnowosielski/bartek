import random

suma = 0
maks = 0
liczba = random.randint(2, 50)

while liczba % 7 != 0 or suma == 0:
    suma += liczba
    if liczba > maks:
        maks = liczba

    liczba = random.randint(2, 50)
    print(liczba)


print("suma liczb to:", suma)
print("wartość maksymalna to:", maks)


