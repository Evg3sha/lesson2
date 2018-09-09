def ask_user():
    questions = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Сижу', 'На чем сидишь?': 'На стуле',
                 'На каком из двух?': 'Умри'}
    while True:
        user_input = input('Задай вопрос: ')
        if user_input in questions:
            print(questions[user_input])
        elif user_input == 'Пока':
            break
        else:
            print('Не знаю')


ask_user()
