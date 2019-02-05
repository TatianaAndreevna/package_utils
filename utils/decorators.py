from datetime import datetime


def decorator(path):
    def logger(foo):
        def info(*args, **kwargs):
            result = foo(*args, **kwargs)
            with open(path + 'result.txt', 'a', encoding='utf-8') as f:
                f.write('{} {} {} {} {}\n'.format(datetime.now(), foo.__name__, args, kwargs, result))
            print(datetime.now(), foo.__name__, args, kwargs, result)
            return result
        return info
    return logger


@decorator('C:\\Users\\Пользователь\\PycharmProjects\\Decorators\\')
def my_function(*args, multi=3):
    return args * multi


my_function('x', 'y', 'z', multi=6)