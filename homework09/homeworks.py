# task 1
print("# task 1")
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


# task 2 (HW 6)
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


# task 3 (HW 5)
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)
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
    print(result_list)
    return result_list


# task 4 (HW 4)
# У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
def change_1_and_5_element(people_records):
    """
    Return the list in which changed 1 and 5 element
    :param people_records: List of people with params(first name, second name, age, master degree, city)
    """
    # people_records = [('John', 'Doe', 28, 'Engineer', 'New York'),
    #                   ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    #                   ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    #                   ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    #                   ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    #                   ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    #                   ('David', 'Miller', 33, 'Software Developer', 'Austin')]

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
    print(modified_list)
    return modified_list


# task 5 (HW 03_02)

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

# task 6 (HW 07)
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

# task 7 (HW 07)
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
