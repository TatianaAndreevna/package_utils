from utils.generators import my_generators
from utils.context_manager import Time


def adv_print(*args, start='', sep='\n', max_line=5, in_file=False):

    if not args:
        return start
    for text in args:
        if len(start + text) > max_line:
            result = (start + text)[:max_line] + '\n'
            print_line = start + text
            while len(print_line) >= max_line:
                print_line = print_line[max_line:]
                result += print_line[:max_line] + '\n'
            print(result + sep)
            if in_file:
                with open('file.txt', 'a', encoding='utf-8') as f:
                    f.write(result)
        else:
            result = start + text + sep
            print(result)
            if in_file:
                with open('file.txt', 'a', encoding='utf-8') as f:
                    f.write(result)
    for item in my_generators('C:\\Users\\Пользователь\\PycharmProjects\\package_utils\\file.txt'):
        print(item)



if __name__ == '__main__':
    with Time():
        adv_print('абвгдеёжз', 'клмнопрст', 'уфхцчшщ', sep='\n', max_line=7, in_file=True)