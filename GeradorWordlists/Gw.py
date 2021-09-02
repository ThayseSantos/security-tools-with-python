import itertools


string = input('String a ser permutada: ')


resultado = itertools.permutations(string, len(string))

for i in itertools.product(string, repeat=len(string)):
    print(''.join(i))
