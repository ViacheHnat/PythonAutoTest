# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# task 1
print("# task 1")


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0

    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_numbers(num1, num2):
    return eval("num1 + num2")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_value(*args):
    sum_num = 0
    for number in args:
        sum_num += number
    avr_val = sum_num / args.__len__()
    return avr_val


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def revers_str(srtr):
    new_str = srtr[::-1]
    return new_str


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(list_of_words):
    longest_word = ''
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


# task 6
print("# task 6")
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


# task 7 (HW 6)
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
def sum_of_even_numbers(list_of_numbers):
    """The def return sum of all even numbers
    :param list_of_numbers: list of numbers
    :return: sum of even numbers
    """
    sum_of_even_numbers = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            sum_of_even_numbers += number
    print("Сума парних чисел =", sum_of_even_numbers)
    return sum_of_even_numbers


# task 8 (HW 5)
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements

def myFunc(e):
    return e[1]


def return_first_5_car_in_list(car_data, search_criteria):
    """
    Return first 5 elements(cars name) from the list
    :param car_data: Exists some car data with color, year, engine_volume, car type , price
    :param search_criteria: Search_criteria as tuple of ( year>= , engine_volume >= , price<=)
    """
    result_list = list()
    result = list()
    for name, characters in car_data.items():
        if characters.__getitem__(1) >= search_criteria.__getitem__(0) and characters.__getitem__(
                2) >= search_criteria.__getitem__(1) and characters.__getitem__(4) <= search_criteria.__getitem__(2):
            lll = [name, characters.__getitem__(4)]
            result.append(lll)
    result.sort(key=myFunc)
    if result.__len__() == 0:
        print("Немає співпадінь")
    else:
        for i in range(5):
            result_list.append(result[i][0])
    return result_list


# task 9 (HW 4)
# У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
def change_1_and_5_element(people_records):
    """
    Return the list in which changed 1 and 5 element
    :param people_records: List of people with params(first name, second name, age, master degree, city)
    """
    modified_list = list()
    first_index = 1
    second_index = 5
    for x in range(people_records.__len__()):
        if x == first_index:
            modified_list.append(people_records[second_index])
        elif x == second_index:
            modified_list.append(people_records[first_index])
        else:
            modified_list.append(people_records[x])
    return modified_list


# task 10 (HW 03_02)

# Виведіть, скільки слів у тексті починається з Великої літери?
def count_word_start_upper_case(adwentures_of_tom_sawer):
    """
    Return count upper letter in str adwentures_of_tom_sawer
    :param adwentures_of_tom_sawer: str
    :return: int
    """
    i = 0
    for letter in adwentures_of_tom_sawer:
        if letter.isupper():
            i = i + 1
    return i


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# Додаткові завдання (За бажанням):

# Рядок відформатованої дати:
# Ваше завдання - написати функцію, яка отримує дату у вигляді трьох чисел: день, місяць та рік та має на
# вході розподілювач за замовчанням - "." функція повертає рядок у вигляді "день.місяць.рік".
# Наприклад, для дати 15 березня 2023 року функція
# повинна повертати рядок "15.03.2023". Якщо користувач задає сепаратор відмінний від звичайного, наприклад '/',
# то функція повертає "15/03/2023"
# Підказка: допоможе використання методу .join():

# My version
def formating_data_vers1(day, month, year, sep='.'):
    return f'{day}{sep}{month}{sep}{year}'


# Version with join
def formating_data_vers2(day, month, year, sep='.'):
    myTuple = (str(day), str(month), str(year))
    formating_data_str = sep.join(myTuple)
    return formating_data_str


# Порівняння словників:
# Ваше завдання - написати функцію, яка порівнює два словника, представляючи оцінки студентів за курси.
# Кожен словник має структуру {'ПІБ студента': оцінка}.
# Функція повинна порівнювати оцінки студентів за кожний предмет та повертати словник
# з різницею в оцінках для кожного студента.
#
# ```
# def compare_grades(grades1, grades2):
#     # Ваш код тут
#     pass
# ```
#
# # Приклад використання функції:
grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Машка': 15}
grades_2 = {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80, 'Пашка': 12}


#
# result = compare_grades(grades_1, grades_2)
# print(result)
# # Можливий вивід: {'Анна Коваленко': -2, 'Олег Петров': -2, 'Ірина Сидорова': -2}
#
# Вимоги:
#     Функція повинна приймати два аргументи — словники з оцінками студентів (grades1 та grades2).
#     Функція повинна порівнювати оцінки за кожним ключем (ПІБ студента) та повертати словник, в якому ключами є
#     ПІБ студентів, а значеннями — різниця в оцінках між grades1 та grades2.
#     Виведіть результат для прикладу використання функції.
#     Перевірте функцію на кількох тестових вхідних даних, включаючи випадки,
#     коли студенти отримали різні оцінки або коли є студенти, які взагалі не мають оцінок в одному зі словників.

def compare_grades(grades_1, grades_2):
    grade_list = []
    for student in grades_1:
        if grades_2.get(student) is None:
            grade_list.insert(1, (student, "None in grades_2"))
            break
        else:
            result = grades_1.get(student) - grades_2.get(student)
            grade_list.insert(1,(student, result))
    for student in grades_2:
        if grades_1.get(student) is None:
            grade_list.insert(1, (student, "None in grades_1"))
    return grade_list

result = compare_grades(grades_1, grades_2)
print(result)
