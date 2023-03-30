import random

def create_list():
    new_list = [random.randint(random.randint(0,10), random.randint(10,20)) for _ in range(random.randint(10,20))]
    return new_list

def find_index_in_range(find_list, min_value, max_value):
    index_list = []
    for i in range(len(find_list)):
        if min_value <= find_list[i] <= max_value:
            index_list.append(i)
    return index_list


list_1 = create_list()
print(list_1)
print(find_index_in_range(list_1, int(input("Введите минимальное число: ")), int(input("Введите максимальное число: "))))

