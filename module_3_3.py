# Распаковка позиционных параметров

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, '2', 8)
print_params(11)
print_params(b='Another string')

values_list = [[1, 2], 'Hello, world!', 5]
values_dict = {'a': False, 'b': 23, 'c': 'Ok'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Urban', True]

print_params(*values_list_2, 42)
