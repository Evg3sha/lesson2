def get_activity(age):
    if age < 7:
        return 'Go to the kindergarten'
    elif 7 <= age < 18:
        return 'Go to the school'
    elif 18 <= age < 23:
        return 'Go to the university'
    else:
        return 'Go to the work'


user_age = int(input('Введите свой возраст:'))
activity = get_activity(user_age)
print(activity)
