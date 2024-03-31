# from multiprocessing.pool import worker
import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print('task 01')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer, end="\n\n")

# task 02 ==
""" Замініть .... на пробіл
"""
print('task 02')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer, end="\n\n")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('task 03')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(adwentures_of_tom_sawer, end="\n\n")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('task 04')
print('Літера "h" зустірчаєтьсяється', adwentures_of_tom_sawer.lower().count("h"), 'разів', end="\n\n")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('task 05')
i = 0
for letter in adwentures_of_tom_sawer:
    if letter.isupper():
        i = i + 1
print('Кількість слів що починається з Великої літери:', i, end="\n\n")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print('task 06')
start = 0
for i in range(2):
    start = adwentures_of_tom_sawer.find("Tom", start)
    if i < 1:
        start = +1
    else:
        print("Позицію, на якій слово Tom зустрічається вдруге -", start, end="\n\n")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print('task 07')
adwentures_of_tom_sawer_sentences = re.split('[.!?]', adwentures_of_tom_sawer)
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence == "":
        adwentures_of_tom_sawer_sentences.remove(sentence)
print(adwentures_of_tom_sawer_sentences, end="\n\n")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print('task 08')
print(adwentures_of_tom_sawer_sentences[3].lower().strip(), end="\n\n")
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print('task 09')
result = False
for element_from_list in adwentures_of_tom_sawer_sentences:
    if element_from_list.strip().startswith("By the time"):
        result = True
        break
if result:
    print("Так, є таке речення", end="\n\n")
else:
    print("Немає такого речення", end="\n\n")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print('task 10')
list_len = adwentures_of_tom_sawer_sentences.__len__() - 1
spleeting_last_sentence = adwentures_of_tom_sawer_sentences[list_len].split()
print("Кількість слів останнього речення з adwentures_of_tom_sawer_sentences -", spleeting_last_sentence.__len__())
