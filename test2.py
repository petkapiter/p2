username = input('Введите имя пользователя: ')
password = input('Введите парлоль: ')

password_correct = False

while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
        password = input('Введите парлоль: ')
    else:
        print(f'Пароль для пользователя {username} установлен')
        password_correct = True