def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def divis(a,b):
    return a/b

def mult(a,b):
    i=1
    mult=0
    while i<=b:
        mult+=a
        i+=1
    return mult

def Fact(a):
    fact=1
    i=1
    while i<=a:
          fact=mult(fact,i)
          i+=1    
    return fact

def Power(a,b):
    i=1
    power=1
    while i<=b:
        power=power*a
        i+=1
    return power

def Log(a,b):
    i=0
    while a>1:
        a=a/b
        i+=1
    return i

def Sqrt(a):
    i=0
    while i*i!=a:
        i+=1
        if i*i==a:
            return i

print('Это простой калькулятор.')
number=int(input('Выбери действие и цифру. 1)+, 2)-, 3)*, 4)/, 5)√, 6)^, 7)log. '))

if number==1:
    a=float(input('Введите первое слагаемое: '))
    b=float(input('Введите второе слагаемое:'))
    print('Сумма чисел равна', add(a,b))

if number==2:
    a=float(input('Введите уменьшаемое: '))
    b=float(input('Введите вычитаемое:'))
    print('Разность равна', substract(a,b))
    
if number==3:
    a=float(input('Введите первый множитель: '))
    b=float(input('Введите второй множитель:'))
    print('Произведение раавно', mult(a,b))

if number==4:
    a=float(input('Введите делимое: '))
    b=float(input('Введите делитель:'))
    print('Частное равно', divis(a,b))
    
if number==5:
    a=float(input('Введите число, из которого нужно извечь корень: '))
    print('Полученное число равно', Sqrt(a))

if number==6:
    a=float(input('Введите степень: '))
    b=float(input('Введите показатель:'))
    print('Полученное число равно', Power(a,b))

if number==7:
    a=float(input('Введите логарифмируемое число: '))
    b=float(input('Введите основание логарифма:'))
    print('Полученное число равно', Log(a,b)
