import threading

from rule_based_bots.shoot_closest import ShootClosestBot
from rule_based_bots.shoot_lowest_life import ShootLowestLifeBot

if __name__ == '__main__':
    threading.Thread(target=ShootClosestBot(1).run).start()
    threading.Thread(target=ShootLowestLifeBot(2).run).start()
