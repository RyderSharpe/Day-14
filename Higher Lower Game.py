# https://www.higherlowergame.com/

import random
from game_data import data

random_dict = random.choice(data)
a = random_dict['name']
b = random_dict['follower_count']
#print(a, b)
print(b)


random_dict_2 = random.choice(data)
c = random_dict_2['name']
d = random_dict_2['follower_count']
#print(c, d)
print(d)

def compare(b,d):
    if b > d:
        #return 'b'
        print(b)
    else:
        #return 'd'
        print(d)

compare(b,d)
