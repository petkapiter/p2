try:
    a = input("Введите a:")
    b = input("Введите b:")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так!")
else:
    print("Результат в квадрате {}".format(result**2))
finally:
    print("Это всё")