people_records = [('John', 'Doe', 28, 'Engineer', 'New York'),
                  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
                  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
                  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
                  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
                  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
                  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
                  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
                  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
                  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
                  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
                  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
                  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
                  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
                  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')]

# 1 - Додайте свій новий запис на початок даного списку
people_records.insert(0, ('Oompa', 'Loompas', 213, 'Joga master', 'Pygmy'))

# 2 - У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
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

# 3 - Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30. Виведіть результат перевірки

check_index = (6, 10, 13)

# Decision 1
check_age_list = list()
result_test_age1 = True
for i in check_index:
    check_age_list.append(modified_list[i][2])
for age in check_age_list:
    if age >= 30:
        pass
    else:
        result_test_age1 = False
        break
print("Decision 1")
if result_test_age1: print("All users almost retired")
if not result_test_age1: print("We have teenager")

# Decision 2
result_test_age2 = True
for i in check_index:
    age = modified_list[i][2]
    if age >= 30:
        pass
    else:
        result_test_age2 = False
        break
print("Decision 2")
if result_test_age2: print("All users almost retired")
if not result_test_age2: print("We have teenager")
