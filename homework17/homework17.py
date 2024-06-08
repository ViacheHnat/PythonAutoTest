# Генератори
# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
import logging


def pair_number():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
            i += 1
        elif i % 2 != 0:
            i += 1


# gen = pair_number()
# for _ in range(6):
#     print(next(gen))


# Генератори
# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_generator(stop_number):
    a, b = 0, 1
    while a <= stop_number:
        yield a
        a, b = b, a + b
    if a > stop_number:
        raise StopIteration('Aстанавитесь!')


# fib = fibonacci_generator(5)
# for _ in range(53):
#     print(next(fib))


# Ітератори
# 1.Реалізуйте ітератор для зворотного виведення елементів списку.
class MyIteratorFromEnd:

    def __init__(self, list_iter):
        self.end_num = 0
        self.list = list_iter
        self.current = list_iter.__len__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end_num:
            self.current -= 1
            return self.list[self.current]
        else:
            raise StopIteration('Aстанавитесь!')


# Ітератори
# 2.Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class MyIteratorPair:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        print("Парні числа:", )
        while self.current <= self.max_num:
            if self.current % 2 == 0:
                print(self.current)
                self.current += 1
            elif self.current % 2 != 0:
                self.current += 1
            elif self.current > self.max_num:
                raise StopIteration


# my_iterator = MyIteratorPair(5)
# my_iterator.__next__()


# Декоратори
# 1. Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_event1(str1: str, str2: str, result: str):
    # def log_event(username: str, status: str):

    log_message = f"{str1}, {str2}, {result}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
    logger = logging.getLogger("log_event")
    logger.info(log_message)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_event1(args, kwargs, result)
        return result

    return wrapper

@log_decorator
def test_example():
    # Тестові перевірки
    pass


test_example()


# Декоратори
# 2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def my_decorator2(func):
    def wrapper():
        try:
            func()
        except Exception:
            print("claas")

    return wrapper

# @my_decorator2
# def teste():
#     u = 7/0
# teste()
