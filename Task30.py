def create_subsequence(number, difference, quantity):
    new_list = [i for i in range(number, (number+(quantity - 1)*difference)+1, difference)]
    return new_list

print(create_subsequence(int(input("Введите первое число последовательности: ")),
                         int(input("Введите разность между числами последовательности: ")),
                         int(input("Введите длину последовательности: "))))