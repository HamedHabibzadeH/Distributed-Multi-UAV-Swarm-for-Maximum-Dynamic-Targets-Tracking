import numpy as np

class Target:
    def __init__(self, x, y, radius=10, color=(0, 0, 255)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color  # BGR

class UAV:
    def __init__(self, x, y, yaw=0.0, has_camera=False):
        self.x = x
        self.y = y
        self.yaw = yaw  # زاویه جهت‌گیری (رادیان)
        self.has_camera = has_camera
        
        # تاریخچه برای رسم یا دیباگ
        self.trajectory = []

    def update(self, v, yaw_rate, dt=0.1, bounds=(800, 600)):
        # حرکت با سرعت خطی ثابت و کنترل سرعت چرخشی (yaw_rate)
        self.yaw += yaw_rate * dt
        self.x += v * np.cos(self.yaw) * dt
        self.y += v * np.sin(self.yaw) * dt
        
        # محدود کردن داخل صفحه
        self.x = np.clip(self.x, 20, bounds[0] - 20)
        self.y = np.clip(self.y, 20, bounds[1] - 20)
        
        self.trajectory.append((self.x, self.y))
