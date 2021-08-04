import json
import requests


class Comm:
    def __init__(self, ip, bot_number):
        self.ip = ip
        self.cmd = {'botNo': bot_number}
        self.session = requests.Session()
        self.reset_cmd()

    def send(self):
        ip, port = self.ip, '8080'
        url = f'http://{ip}:{port}/cmd'

        raw = self.session.post(url, json=self.cmd)
        status = json.loads(raw.text)
        self.reset_cmd()

        return status

    def rotate(self, angle):
        if angle < 0.:
            angle = -1
        if angle > 0.:
            angle = 1
        self.cmd['rotation'] = angle

    def move(self, dx, dy):
        if dx < 0.:
            dx = -1
        if dx > 0.:
            dx = 1
        self.cmd['dx'] = dx

        if dy < 0.:
            dy = -1
        if dy > 0.:
            dy = 1
        self.cmd['dy'] = dy

    def shoot(self, val):
        val = True if val else False
        self.cmd['shoot'] = val

    def reset_cmd(self):
        self.cmd['dx'] = 0
        self.cmd['dy'] = 0
        self.cmd['rotation'] = 0
        self.cmd['shoot'] = False
