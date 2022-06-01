from random import randint

def random_list():
    r = [randint(a, b) for i in range(c)]
    print(r)

a = int(input("Укажите начало диапазона: "))
b = int(input("Укажите конец диапазона: "))
c = int(input("Количество элементов: "))

random_list()

