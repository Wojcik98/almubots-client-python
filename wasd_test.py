import sys
import termios
import tty

from utils.almubots_comm import Comm


class WASDBot:
    def __init__(self, bot_num):
        self.bot_num = bot_num
        self.comm = Comm(bot_num)

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def run(self):
        while True:
            ch = self.getch()

            if ch == '\x03':
                raise KeyboardInterrupt

            rot = 0
            if ch == 'e':
                rot = 1
            elif ch == 'q':
                rot = -1
            self.comm.rotate(rot)

            dy = 0
            if ch == 'w':
                dy = 1
            elif ch == 's':
                dy = -1

            dx = 0
            if ch == 'a':
                dx = -1
            elif ch == 'd':
                dx = 1

            self.comm.move(dx, dy)

            shoot = False
            if ch == ' ':
                shoot = True
            self.comm.shoot(shoot)

            print(self.comm.send())
