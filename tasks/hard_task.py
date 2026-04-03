from env.traffic_env import TrafficEnv
import random

class HardTrafficTask(TrafficEnv):
    def spawn_cars(self):
        self.north_queue += random.randint(1, 3)
        self.south_queue += random.randint(1, 3)
        self.east_queue += random.randint(1, 3)
        self.west_queue += random.randint(1, 3)

    def spawn_emergency(self):
        if self.emergency is None and random.random() < 0.1:
            self.emergency = random.choice(["N", "S", "E", "W"])