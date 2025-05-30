# Day 2: Functions and Data Structures

def square(number: int):
    return number ** 2

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num_list:
    print(square(i))

name_dict = {"name": "John", "age": 25, "city": "New York"}
print(name_dict["name"])
print(name_dict["age"])
print(name_dict["city"])

def sum_of_all_elements(list_num: [int]):
    total = 0
    for i in list_num:
        total += i
    return total

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[2])

def return_even_nums(list_nums: [int]):
    return [i for i in list_nums if i % 2 == 0]
