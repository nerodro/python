def health():
    age = int(input("Введите ваш возвраст"))
    height = int(input("Введите ваш вес"))
    if age < 30 and height > 50 and height < 120:
        print("У вас все хорошо")
    elif age < 30 and height < 50 or height > 120:
        print("Вам следует обратится к врачу")
    elif age > 40 and height < 50 or height > 120:
        print("Вам следует обратится к врачу")
    elif age > 80:
        print("Скоро помирать")
    elif age > 50 and height > 60 or height > 300:
        print("Худеть надо")