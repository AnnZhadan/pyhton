def fun2():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    k = str(a)
    while a < b:
        print("So sad")
        a += c
        k = k + " " + str(a)
    else:
        print("Ura")
        print("Inkrementi:", k)
fun2()