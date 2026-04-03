from env.traffic_env import TrafficEnv
import random

class MediumTrafficTask(TrafficEnv):
    def spawn_cars(self):
        self.north_queue += random.randint(0, 2)
        self.south_queue += random.randint(0, 2)
        self.east_queue += random.randint(0, 2)
        self.west_queue += random.randint(0, 2)