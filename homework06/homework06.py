print("Рахування унікальних символів в строці")
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
list_of_unique_letters = set(input("Введіть символи: "))
print("В списку більше 10 унікальних символів - ", end='')
if list_of_unique_letters.__len__() > 10:
    print("True")
else:
    print("False")
print()
print("Цикл \"Дочекайся літери\"")
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і
# маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
result = True
while result:
    some_list_of_string = set(input("Введіть слово з \"h\" бо \"H\": ").lower())
    for latter in some_list_of_string:
        if latter == "h":
            result = False
            print("Нарешті!!!")
print()
print("Забери зі списку що потрібно")
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for element in lst1:
    if element.__class__ == int:
        lst2.append(element)
print(lst2)
print()
print("Сумуємо числа")
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
sum_of_even_numbers = 0
for number in lst2:
    if number % 2 == 0:
        sum_of_even_numbers += number
print("Сума парних чисел =", sum_of_even_numbers)
