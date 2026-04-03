import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import random
from tasks.easy_task import EasyTrafficTask
import pickle

env = EasyTrafficTask()

with open("q_table.pkl", "rb") as f:
    Q = pickle.load(f)

ACTIONS = ["NS_GREEN", "EW_GREEN", "ALL_RED"]

def get_state(obs):
    return (
        obs["north_queue"],
        obs["south_queue"],
        obs["east_queue"],
        obs["west_queue"],
        obs["signal"]
    )

obs = env.reset()
done = False
total_reward = 0

while not done:
    state = get_state(obs)
    q_values = [Q.get((state, a), 0) for a in ACTIONS]
    action = ACTIONS[q_values.index(max(q_values))]

    obs, reward, done, _ = env.step(action)
    total_reward += reward

print("Trained Agent Reward:", total_reward)