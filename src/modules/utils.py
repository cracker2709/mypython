# arrays
from array import array


def print_sep():
    print('\n###############################\n')


def play_with_array():
    a1 = array('l', [0, 1, 2, 3, 4, 5])
    print(f'{a1}')
    print(a1[2])
    a2 = array('u', ['h', 'e', 'l', 'l', 'o'])
    print(a2[0])
    a2.insert(0, "X")
    print(f'{a2}')


def play_with_lists():
    l0 = [1, 2, 3, 4]
    print(f'l0 : {l0}')
    l1 = ['hello', 42, 'world']
    print(f'l1 : {l1}')
    print(f'{l1[0]} {l1[2]}')
    print(f'{l1[1:]}')
    print(f'At least concatenate lists : {l0 + l1}')

    for var in l0:
        if var < 3:
            print(f'<<<<<< {var} < 3')
        elif var == 3:
            print(f'====== {var} is 3')
        else:
            print(f'>>>>>> {var} > 3')


def play_with_dictionaries():
    d0 = {"mykey1": "myvalue1", "mykey2": "myvalue2"}
    print(d0)
    print(f'Value associated to myKey is {d0["mykey1"]}')
    print(d0.keys())
    print(d0.values())
