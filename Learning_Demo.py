import numpy as np

import gym
from gym.wrappers import TimeLimit

# RENDER_MODE = 'ansi'
RENDER_MODE = 'human'

# Example 1: "4x4", slippery=False
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode='human')

env = TimeLimit(env, 12)

env.metadata["render_fps"] = 3

NUM_EPISODES = 2

demo_policies = np.loadtxt('learning_demo.txt', dtype=int)

# policy = demo_policies[4] # choose from [0, 1, 2, 3, 4]

for i in range(NUM_EPISODES):

    terminated = False
    truncated = False
    state, _ = env.reset()

    while not (terminated or truncated):

        # random policy
        action = env.action_space.sample()

        # action = policy[state]

        next_state, reward, terminated, truncated, info = env.step(action)

        state = next_state

        # Rendering
        if RENDER_MODE == 'ansi':
            print(env.render())
        elif RENDER_MODE == 'human':
            env.render()
        else:
            print('Invalid render mode, only "ansi", "human" args supported' )