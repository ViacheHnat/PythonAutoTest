import unittest
from homework09.homeworks import find_substring, sum_of_even_numbers, return_first_5_car_in_list, car_data, \
    search_criteria, change_1_and_5_element, count_word_start_upper_case, formating_data_vers1, compare_grades


# import homework09.homeworks


class TestTask1(unittest.TestCase):
    def test_return_int_in_substring(self):
        result = find_substring("asdsgdfh", "d")
        print(result)
        self.assertEqual(type(result), int)

    def test_return_index_substring(self):
        result = find_substring("asdsgdfh", "d")
        print(result)
        self.assertEqual(2, result)

    def test_return_fail_substring(self):
        result = find_substring("asdsgdfh", "2")
        print(result)
        self.assertEqual(-1, result)


class TestTask2(unittest.TestCase):
    def testfirs(self):
        result = sum_of_even_numbers([23, 7, 4, 32, 9])
        self.assertEqual(36, result, msg="Result must be 36")

    def test_check_type(self):
        result = sum_of_even_numbers([23, 7, 4, 32, 9])
        print(type(result))
        self.assertEqual(type(result), int)


class TestTask3(unittest.TestCase):
    def testfirs(self):
        result = return_first_5_car_in_list(car_data, search_criteria)
        self.assertEqual(['Toyota', 'Kia', 'Hyundai', 'Mazda', 'Nissan'], result, msg="Different list")

    def test_check_type(self):
        result = return_first_5_car_in_list(car_data, search_criteria)
        print(type(result))
        self.assertEqual(type(result), list)


class TestTask4(unittest.TestCase):
    def testfirs(self):
        result = change_1_and_5_element(people_records=[('John', 'Doe', 28, 'Engineer', 'New York'),
                                                        ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
                                                        ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
                                                        ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
                                                        ('Michael', 'Brown', 22, 'Student', 'Seattle'),
                                                        ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
                                                        ('David', 'Miller', 33, 'Software Developer', 'Austin')])
        expected = [('John', 'Doe', 28, 'Engineer', 'New York'), ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
                    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'), ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
                    ('Michael', 'Brown', 22, 'Student', 'Seattle'), ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
                    ('David', 'Miller', 33, 'Software Developer', 'Austin')]
        self.assertEqual(expected, result)

    def test_check_type(self):
        result = change_1_and_5_element(people_records=[('John', 'Doe', 28, 'Engineer', 'New York'),
                                                        ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
                                                        ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
                                                        ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
                                                        ('Michael', 'Brown', 22, 'Student', 'Seattle'),
                                                        ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
                                                        ('David', 'Miller', 33, 'Software Developer', 'Austin')])
        print(result)
        self.assertEqual(type(result), list)

class TestTask5(unittest.TestCase):
    def test_upper_word(self):
        result = count_word_start_upper_case(adwentures_of_tom_sawer='Ak sdf Kfdfg as')
        print(result)
        self.assertEqual(2, result)

    def test_check_type(self):
        result = count_word_start_upper_case(adwentures_of_tom_sawer='Ak sdf Kfdfg as')
        print(type(result))
        self.assertEqual(type(result), int)


class TestTask6(unittest.TestCase):
    def test_default_separator(self):
        result = formating_data_vers1(12, 2, 1999)
        print(result)
        self.assertEqual('12.2.1999', result)

    def test_separator(self):
        result = formating_data_vers1(12, 2, 1999, "/")
        print(result)
        self.assertEqual('12/2/1999', result)

    def test_check_type(self):
        result = formating_data_vers1(12, 2, 1999)
        print(type(result))
        self.assertEqual(type(result), str)

class TestTask7(unittest.TestCase):
    def testfirs(self):
        result = compare_grades({'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Машка': 15},
                                {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80, 'Пашка': 12})
        expected = [('Анна Коваленко', -2),
                    ('Пашка', 'None in grades_1'),
                    ('Машка', 'None in grades_2'),
                    ('Ірина Сидорова', -2),
                    ('Олег Петров', -2)]
        print(result)
        self.assertEqual(expected, result)

    def test_check_type(self):
        result = compare_grades({'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Машка': 15},
                                {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80, 'Пашка': 12})
        print(type(result))
        self.assertEqual(type(result), list)
