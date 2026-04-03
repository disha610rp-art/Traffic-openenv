import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import random
import pickle
from tasks.easy_task import EasyTrafficTask

env = EasyTrafficTask()

ACTIONS = ["NS_GREEN", "EW_GREEN", "ALL_RED"]

Q = {}

alpha = 0.1
gamma = 0.9
epsilon = 0.2

episodes = 200

def get_state(obs):
    return (
        obs["north_queue"],
        obs["south_queue"],
        obs["east_queue"],
        obs["west_queue"],
        obs["signal"]
    )

for episode in range(episodes):
    obs = env.reset()
    state = get_state(obs)
    done = False
    total_reward = 0

    while not done:
        if random.random() < epsilon:
            action = random.choice(ACTIONS)
        else:
            q_values = [Q.get((state, a), 0) for a in ACTIONS]
            action = ACTIONS[q_values.index(max(q_values))]

        next_obs, reward, done, _ = env.step(action)
        next_state = get_state(next_obs)

        old_q = Q.get((state, action), 0)
        next_max = max([Q.get((next_state, a), 0) for a in ACTIONS])

        new_q = old_q + alpha * (reward + gamma * next_max - old_q)
        Q[(state, action)] = new_q

        state = next_state
        total_reward += reward

    if episode % 20 == 0:
        print("Episode:", episode, "Reward:", total_reward)

with open("q_table.pkl", "wb") as f:
    pickle.dump(Q, f)

print("Training complete. Q-table saved.")