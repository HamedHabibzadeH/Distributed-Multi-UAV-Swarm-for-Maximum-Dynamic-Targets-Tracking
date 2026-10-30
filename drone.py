import math


class Drone:
    def __init__(self, x, y, theta, v):
        self.x = x
        self.y = y
        self.theta = theta
        self.v = v

    def step(self, omega, dt):
        dx = self.v * math.cos(self.theta) * dt
        dy = self.v * math.sin(self.theta) * dt

        self.x += dx
        self.y += dy
        self.theta += omega * dt
