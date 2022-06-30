from game_data import data
from random import randint

def answer(a,b)
    if a > b:
        

play = True
while play:
    item_list = data
    n=len(data)
    picked_item = randint(1,n)
    item1 = item_list.pop(picked_item)


print(len(data))
