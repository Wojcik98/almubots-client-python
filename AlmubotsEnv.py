import gym
from gym import spaces
import numpy as np


class AlmubotsEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, num_of_bots):
        # posX, posY, velX, velY, angle, ammo, life, shoot, score
        low = np.repeat(np.array([0, 0, -500, -500, 0, 0, 0, 0, 0], dtype=np.float32), num_of_bots)
        high = np.repeat(np.array([900, 900, 500, 500, 360, 10, 20, 1, 1000], dtype=np.float32), num_of_bots)

        self.observation_space = spaces.Box(low, high, dtype=np.float32)

        self.action_space = spaces.Discrete(57)

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass


if __name__ == '__main__':
    env = AlmubotsEnv(2)
    print(env.observation_space.high)
