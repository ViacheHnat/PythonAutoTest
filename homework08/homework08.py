some_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def sum_numbers(list_number):
    for data in list_number:
        sum_num = 0
        for num in data.split(','):
            try:
                sum_num = int(num) + int(sum_num)
            except:
                sum_num = "Не можу це зробити"
                break
        print(sum_num)

sum_numbers(some_data)