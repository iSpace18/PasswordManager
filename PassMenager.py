import secrets
file = open('Passwords.txt', 'a+')
file.read()
saving_password = {

}
feedback = """
            menu - меню
            add  - Добавить пароль
            list - показать список паролей
            quit - выход из программы и сохранение всех паролей"""
print(feedback)
programm_is_run = True

while programm_is_run:
    command = input('Введите команду\n')
    command = command.lower()

    #quit
    if command == 'quit':
        print('Выход из программы...')
        exit()

    # menu command

    elif command == 'menu':
        print(feedback)

    #list command

    elif command == 'list':
        print(saving_password)

    #add  command

    elif command == 'add':
        password = ''
        lenght = int(input('Введите длинну пароля: '))

        for x in range(lenght):
            password += secrets.choice(('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))
        print('Сгенерированный пароль: ', password)
        app = input('Для чего вы хотите его использовать? ')
        complete = saving_password.update({app: password})
        key_password = list(saving_password.keys())[-1]
        app_password = list(saving_password.values())[-1]
        complete2 = str(key_password + ':' + app_password)
        file.write(complete2)
        file.write('\n')
    else:
        print('Команда не найдена')
file.close()