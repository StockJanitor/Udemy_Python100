from game_data import data
from random import randint, random


print(len(data))


def chose_item(x):
    # generate item
    num1 = randint(1, len(x)) - 1
    a = x.pop(num1)
    return x, a

list1, item1 = chose_item(data)

def game(list1, item1):
    item1_name = item1["name"]
    item1_follower = int(item1["follower_count"])
    # chekc if you win
    if len(data) == 0:
        print("you win")
        quit()
    # print item 1
    print(f"{item1_name} {item1_follower}")
    # choose item 2
    list2, item2 = chose_item(data)
    item2_name = item2["name"]
    item2_follower = int(item2["follower_count"])
    print(f"{item2_name}")

    # evaluate answer
    answer = input("higher or lower? ")
    if (answer == "higher") and (item2_follower > item1_follower):
        print("correct guess")
        list1, item1 = list2, item2
        game(list1, item1)
        # game again
    elif (answer == "lower") and (item2_follower < item1_follower):
        print("correct guess")
        list1, item1 = list2, item2
        game(list1, item1)
    else:
        print("yoou loose")
        quit()


game(list1, item1)
