def ask_user():
    while True:
        user_answer = input('Как дела?: ')
        if user_answer == 'Хорошо':
            print('Молодец')
            break
        else:
            print('Ну не знаю')
            continue

ask_user()