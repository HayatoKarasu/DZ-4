print("-----------------------------")
print("Перевод числа из десятичного \n   в бинарное состояние")
n = int(input("Введите любое число: "))

def bin_des(n):
    if n >= 2:
        bin_des(n//2)
    print(n % 2, end = " ")
    
    
print("Ваше число в бинарном виде: ")
bin_des(n)
print()

print("-----------------------------")

print("Сумма двух чисел")

def sum(a,b):
    if b==0:
        return a
    return sum(a+1,b-1)
    
    
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Сумма ваших чисел равна:")

print(sum(a, b))
print("-----------------------------")

print("Возведение в степень")

def step(a, b):
    if b <= 0:
        return 1
    elif b == 1:
        return a
    elif b != 1:
        return (a * step(a, b - 1))   
    
    
a = int(input("Введите любое число: "))
b = int(input("Введите степень для этого числа: "))

print("Число", a, "в степени", b, "равно:")
print(step(a, b))
print("-----------------------------")
