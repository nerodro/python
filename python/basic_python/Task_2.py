import datetime

def coordination():
    math = 'y = -12x + 11111140.2121'
    x = 2.5
    name = math.split(' ')
    first_name = str(name[2])
    name[2] = first_name[:-1]
    two_name = float(name[2]) * x + float(name[4])
    print(two_name)

def time():
    day = "20"
    mounth = "10"
    year = "2021"
    data = day,mounth,year
    if day <=0   and day >= 32:
        print("День введен не верно")
    if mounth <= 0 and mounth >= 13:
        print("Месяц введен не верно")
    if year <= 0 and year >= 9999:
        print("Год введен не верно")

def tower():
    print("tower")


