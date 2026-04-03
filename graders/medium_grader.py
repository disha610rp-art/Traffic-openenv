def grade(total_reward, max_reward=800):
    score = total_reward / max_reward
    return max(0.0, min(1.0, score))