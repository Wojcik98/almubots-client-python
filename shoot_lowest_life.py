from math import atan2, pi

from almubots_comm import Comm

botId = 0

if __name__ == '__main__':
    comm = Comm(botId)

    while True:
        status = comm.send()
        me = status['bots'][botId]
        enemy = status['bots'][1]

        for bot in status['bots']:
            if bot is not me and bot['life'] != 0:
                if enemy['life'] > bot['life']:
                    enemy = bot

        alfa = atan2(enemy['y'] - me['y'], enemy['x'] - me['x'])
        alfa = alfa * 180 / pi
        if alfa > me['angle']:
            comm.rotate(1)
        if alfa < me['angle']:
            comm.rotate(-1)

        dx = 0
        dy = 0
        if enemy['x'] > me['x']:
            dx = 1
        if enemy['y'] > me['y']:
            dy = 1
        if enemy['x'] < me['x']:
            dx = -1
        if enemy['y'] < me['y']:
            dy = -1

        comm.move(dx, dy)

        shoot = False
        if abs(me['angle'] - alfa) < 10:
            shoot = True

        comm.shoot(shoot)
