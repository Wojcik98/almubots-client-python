import math


def dist(my_bot, enemy_bot):
    x = my_bot['x'] - enemy_bot['x']
    y = my_bot['y'] - enemy_bot['y']
    return math.sqrt(x * x + y * y)


def sgn(val):
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0
