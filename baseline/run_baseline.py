import random
from tasks.easy_task import EasyTrafficTask
from graders.easy_grader import grade

env = EasyTrafficTask()

obs = env.reset()
done = False
total_reward = 0

ACTIONS = [
    "NS_GREEN",
    "EW_GREEN",
    "ALL_RED"
]

while not done:
    action = random.choice(ACTIONS)
    obs, reward, done, _ = env.step(action)
    total_reward += reward

score = grade(total_reward)

print("Total Reward:", total_reward)
print("Score:", score)