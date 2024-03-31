# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
from _lsprof import profiler_entry

alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\'
#                        '"That depends a good deal on where you want to get to," said the Cat.\'
#                        '"I don\')t much care where ——(" said Alice."
#                                                      "")Then it doesn(\'t matter which way you go,\" said the Cat.\'
#                                                                       '"—— so long as I get somewhere," Alice added as an explanation.\'
#                                                                       '"Oh, you\')re sure to do that," said the Cat, "if you only walk long enough."\'


# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті

# task 03 == Виведіть змінну alice_in_wonderland на друк
# print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print('task 04')
black_sea_square = 436402
sea_of_azov_square = 37800
sum_square = black_sea_square + sea_of_azov_square
print("Сумарна площа: {}\n".format(sum_square))

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print('task 05')
all = 375291
sum_first_and_second = 250449
sum_second_and_third = 222950
first = all - sum_second_and_third
second = sum_first_and_second - first
third = all - sum_first_and_second
# print(f'Перший склад: {first}\n'
#       f'Другий склад: {second}\n'
#       f'Третій склад: {third}\n')
print(f'''Перший склад: {first}
Другий склад: {second}
Третій склад: {third}\n''')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print('task 06')
per_month = 1179
count_month = 18
cost = per_month * count_month
print("Вартість комп'ютера:", cost, "грн", end="\n\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('task 07')
text = "Остача при діленні"
print("a)", text, "8019 на 8 = " + str(8019 % 8))
print("b)", text, "9907 на 9 = " + str(9907 % 9))
print("c)", text, "2789 на 5 = " + str(2789 % 5))
print("d)", text, "7248 на 6 = " + str(7248 % 6))
print("e)", text, "7128 на 5 = " + str(7128 % 5))
print("f)", text, "19224 на 9 = " + str(19224 % 9))
print()
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print('task 08')
print("Сума замовлення:", 4 * 274 + 2 * 218 + 4 * 35 + 350 + 3 * 21, "\nБез врахування вартості доставки та чайових\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print('task 09')
count_photo = 232
on_the_page = 8
page_count = 0
if count_photo % on_the_page == 0:
    page_count = count_photo // on_the_page
else:
    page_count = count_photo // on_the_page + 1
page_count_to_str = "Потрібно " + page_count.__str__() + " сторінок"
print(page_count_to_str)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print()
print('task 10')
distance = 1600
interval = 100
fuel_consumption = 9
tank_capacity = 48

total_fuel_for_trip = (distance / interval) * fuel_consumption
print("Для подорожі необхідно " + total_fuel_for_trip.__str__()+" літри")
pitstop_count = 0
if (total_fuel_for_trip%tank_capacity==0):
    pitstop_count = total_fuel_for_trip / tank_capacity - 1
else:
    pitstop_count = total_fuel_for_trip / tank_capacity
print("Необхідно:", pitstop_count.__int__(), "зупинок(ки)")