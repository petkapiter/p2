try:
    a = input("Введите a:")
    b = input("Введите b:")
    print("Результат:", int(a)/int(b))
except ValueError:
    print("Пожалуйста, вводите только числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")