from modules.datemodule import get_date

def writeinFile(filename):
    to_append=('abc', 'def')
    with open(filename, 'w') as f:
        f.write(get_date() + "\n")
        for item in to_append:
            f.write(item + '\n')

def viewfile(filename):
    with open(filename, 'r') as f:
        for service in f:
            print(service)