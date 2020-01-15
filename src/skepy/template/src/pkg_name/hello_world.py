import os


def greeting():
    dir_name = os.path.dirname(__file__)
    with open(os.path.join(dir_name, 'data', 'hello.txt'), 'r') as f:
        print(f.read())
