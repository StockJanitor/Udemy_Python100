from game_data import data
from random import randint, random


print(len(data))


def chose_item(x):
    # generate item
    num1 = randint(1, len(x)) - 1
    a = x.pop(num1)
    return x, a


def determine(x, y, z):
    # x = user input, y = list, z = item

    return


list1, item1 = chose_item(data)


def game():
    list2, item2 = chose_item(data)

    answer = input("higher or lower? ")
    if (answer == "higher") and (b > a):
        chose_item(x, y)
    elif (answer == "lower") and (b < a):
        chose_item(x, y)
    else:
        print("yoou loose")

    # x.pop()
    # print(a)
    # print(len(x))
    # b = x.pop[chose_num(x)]
    # print(b)
    # print(len(x))


# return 2 selected item
# answer
# if correct >> game else end >>

# def answer(a,b)
#     if a > b:


# play = True
# while play:
#     item_list = data
#     n=len(data)
#     picked_item = randint(1,n)
#     item1 = item_list.pop(picked_item)


# print(len(data))
chose_item(data)
print(len(data))
