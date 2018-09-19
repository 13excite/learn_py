def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError as err:
        print(f" Value Error: {err}")


print(get_summ("ss", 'ss'))
print(get_summ(2.3, 3))
print(get_summ(1, '3'))
print(get_summ('aa', 3))