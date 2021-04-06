#Тараканов Никита
#Тема 2.1 Ветвления
#Текстовые задачи

def Zadacha_1():
    a = -5
    b = 8
    c  = 5
    print(a**4,b**2,c**2)

def Zadacha_2():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    if x1 > x2 or y1 > y2:
        print("A > B")
    else:
        print("B > A")

def Zadacha_3():
    b = 60
    a = 100
    if a + b < 180:
        print("Да возможен")
    else:
        print("Нет такой не возможен")
    if a or b == 90:
        print("Треугольник прямоугольный")
    else:
        print("Нет не прямоугольный")

def Zadacha_4():
    x = 6
    y = 8
    x = x + y / 2
    y = x + y * 2

def Zadacha_5():
    x = 0
    y = 0
    if x < 0:
        print("Точка отрицательная")
    elif x > 0:
        print("Точка положительная")

def Zadacha_6():
    m = 6
    n = 5
    if m > n:
        n = m
    elif n > m:
        m = n
    elif m == n:
        m,n = 0

def Zadacha_7():
    a = -4
    b = -6
    c = 1
    while True:
        i  = 0
        if a or b or c < 0:
            i = i+1
            print(i)

def Zadacha_8():
    a = -4
    b = -6
    c = 1
    while True:
        i = 0
        if a or b or c > 0:
            i = i + 1
            print(i)

def Zadacha_9():
    a = -4
    b = -6
    c = 1
    while True:
        i = 0
        if a or b or c != float:
            i = i + 1
            print(i)

def Zadacha_10():
    a = 8
    c = 6
    b = 2
    k = 3
    if a //k == 0:
        print(a)
    elif b // k ==0:
        print(b)
    elif c // k ==0:
        print(c)