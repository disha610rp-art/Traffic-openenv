import random

class TrafficEnv:
    def __init__(self):
        self.max_steps = 100
        self.reset()

    def reset(self):
        self.north_queue = random.randint(0, 5)
        self.south_queue = random.randint(0, 5)
        self.east_queue = random.randint(0, 5)
        self.west_queue = random.randint(0, 5)

        self.emergency = None
        self.signal = "ALL_RED"
        self.time_step = 0

        return self.get_observation()

    def state(self):
        return self.get_observation()

    def get_observation(self):
        return {
            "north_queue": self.north_queue,
            "south_queue": self.south_queue,
            "east_queue": self.east_queue,
            "west_queue": self.west_queue,
            "signal": self.signal,
            "emergency": self.emergency,
            "time_step": self.time_step
        }

    def spawn_cars(self):
        self.north_queue += random.randint(0, 2)
        self.south_queue += random.randint(0, 2)
        self.east_queue += random.randint(0, 2)
        self.west_queue += random.randint(0, 2)

    def spawn_emergency(self):
        if self.emergency is None and random.random() < 0.05:
            self.emergency = random.choice(["N", "S", "E", "W"])

    def move_cars(self):
        cars_passed = 0
        emergency_passed = False

        if self.signal == "NS_GREEN":
            if self.north_queue > 0:
                self.north_queue -= 1
                cars_passed += 1
            if self.south_queue > 0:
                self.south_queue -= 1
                cars_passed += 1
            if self.emergency in ["N", "S"]:
                emergency_passed = True
                self.emergency = None

        elif self.signal == "EW_GREEN":
            if self.east_queue > 0:
                self.east_queue -= 1
                cars_passed += 1
            if self.west_queue > 0:
                self.west_queue -= 1
                cars_passed += 1
            if self.emergency in ["E", "W"]:
                emergency_passed = True
                self.emergency = None

        return cars_passed, emergency_passed

    def compute_reward(self, cars_passed, emergency_passed, signal_changed):
        waiting_cars = (
            self.north_queue +
            self.south_queue +
            self.east_queue +
            self.west_queue
        )

        reward = 0
        reward += cars_passed
        reward -= waiting_cars * 0.2

        if emergency_passed:
            reward += 10

        if self.emergency is not None:
            reward -= 5

        if signal_changed:
            reward -= 1

        return reward

    def step(self, action):
        old_signal = self.signal
        self.signal = action
        signal_changed = old_signal != action

        cars_passed, emergency_passed = self.move_cars()

        self.spawn_cars()
        self.spawn_emergency()

        reward = self.compute_reward(
            cars_passed,
            emergency_passed,
            signal_changed
        )

        self.time_step += 1
        done = self.time_step >= self.max_steps

        observation = self.get_observation()

        return observation, reward, done, {}