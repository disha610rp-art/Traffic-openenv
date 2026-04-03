from env.traffic_env import TrafficEnv
import random

class EasyTrafficTask(TrafficEnv):
    def spawn_emergency(self):
        self.emergency = None

    def spawn_cars(self):
        self.north_queue += random.randint(0, 1)
        self.south_queue += random.randint(0, 1)
        self.east_queue += random.randint(0, 1)
        self.west_queue += random.randint(0, 1)