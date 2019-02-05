import hashlib


def my_generators(path):
    with open(path) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for item in my_generators('C:\\Users\\Пользователь\\PycharmProjects\\iterators\\c_file.txt'):
    print(item)