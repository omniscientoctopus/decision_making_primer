import gym

# RENDER_MODE = 'ansi'
RENDER_MODE = 'human'

# Example 1: "4x4", slippery=False
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode='human')

# Example 2: "4x4", slippery=True
# env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True, render_mode='human')

# Example 3: "8x8", slippery=True
# env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=True, render_mode='human')

# Example 4: Random map of size=8, True
# Feel free to increase/decrease map size or set the is_slippery flag to True/False
# env = gym.make('FrozenLake-v1', desc=generate_random_map(size=8), is_slippery=True, render_mode=RENDER_MODE)

env.metadata["render_fps"] = 3

NUM_EPISODES = 6

# For example 1
optimal_policy_1 = [2, 2, 1, 0, 1, 3, 1, 1, 2, 2, 1, 2, 1, 2, 2, 3]
optimal_policy_2 = [1, 2, 1, 0, 1, 3, 1, 3, 2, 2, 1, 1, 3, 2, 2, 1]
optimal_policy_3 = [1, 2, 1, 0, 1, 1, 1, 0, 2, 1, 1, 0, 2, 2, 2, 3]

for i in range(NUM_EPISODES):

    terminated = False
    state, _ = env.reset()

    while not terminated:

        # random policy
        action = env.action_space.sample()

        # optimal policy 1
        # action = optimal_policy_1[state]
        
        # optimal policy 2
        # action = optimal_policy_2[state]

        # optimal policy 3
        # action = optimal_policy_3[state]

        next_state, reward, terminated, _, info = env.step(action)

        state = next_state

        # Rendering
        if RENDER_MODE == 'ansi':
            print(env.render())
        elif RENDER_MODE == 'human':
            env.render()
        else:
            print('Invalid render mode, only "ansi", "human" args supported' )