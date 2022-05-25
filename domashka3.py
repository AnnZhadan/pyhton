def fun3():
    a = int(input("Напишіть значення для а: "))
    b = int(input("Напишіть значення для b: "))
    c = int(input("Напишіть значення для c: "))

    if a > b:
        print("Сумний результат для нашої b.")
    elif b > a and b > c:
        print("Ура ура b чемпіон!")
    elif a == b:
        print("Рівноправність у родині a та b.")
    else:
        print("Ну таке")

