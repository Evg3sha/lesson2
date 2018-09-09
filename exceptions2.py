def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return None


print(get_summ(2, '5'))