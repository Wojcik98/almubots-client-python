import sys
import termios
import tty

from almubots_comm import Comm


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == '__main__':
    comm = Comm('192.168.1.123', 1)

    while True:
        ch = getch()

        if ch == '\x03':
            raise KeyboardInterrupt

        rot = 0
        if ch == 'e':
            rot = 1
        elif ch == 'q':
            rot = -1
        comm.rotate(rot)

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

        comm.move(dx, dy)

        shoot = False
        if ch == ' ':
            shoot = True
        comm.shoot(shoot)

        print(comm.send())
