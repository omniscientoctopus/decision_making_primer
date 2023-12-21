"""
This environment is an adaption of Frozen Lake gym environment.

https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py

Differences:
- Here we only have deterministic actions.
- we use the simpler reward model R(s) instead of R(s,a,s').
- Currently only supports a 4x4 map.

"""
import numpy as np
import gym

from gym.spaces import Discrete

class FrozenLake(gym.Env):

    def __init__(self, num_rows=4, num_cols=4, prob_slip=None) -> None:
        super().__init__()

        self.state = 0

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.num_states = num_rows*num_rows
        self.num_actions = 4

        self.observation_space = Discrete(self.num_states)
        self.action_space = Discrete(self.num_actions)

        self.prob_slip = prob_slip
        self.windy = False if prob_slip is None else True

        # reset env when object is created
        self.reset()

    def transition_model(self, state, action):

        """
        This function defines the transition model of the MDP.

        Input
        -----
        state: int
            One of the states in the grid
            [0, ..., 15]
        action: int
            One of four possible actions
            [0, 1, 2, 3]

        """

        prob = 1 # we have deterministic transitions

        # holes or terminal states
        # agent remains there and episode terminates
        if state in [5, 7, 11, 12, 15]:
            # state does not change
            next_state = state
            done = True

            return [[prob, next_state, done]]
        
        # get row and col of state
        row, col = divmod(state, self.num_rows)

        # action map
        if action == 0: # left
            col = max(col - 1, 0)
        elif action == 1: # down
            row = min(row + 1, self.num_rows - 1)
        elif action == 2: # right
            col = min(col + 1, self.num_cols - 1)
        elif action == 3: # up
            row = max(row - 1, 0)

        intended_state = row * self.num_rows + col
        done = False
    
        # stochastic setting
        if self.windy:

            # probability of moving to intended square
            prob_no_slip = 1 - self.prob_slip

            # prob slipping
            prob_slip = self.prob_slip

            # move up two row if action = up
            if action == 3: # up
                _unintended_row = max(row - 2, 0)
            else:
                _unintended_row = max(row - 1, 0)

            _unintended_state = _unintended_row * self.num_rows + col

            return [[prob_no_slip, intended_state, done], [prob_slip, _unintended_state, done]]

        # no winds (simple deterministic setting)
        else:
            return [[prob, intended_state, done]]

    @staticmethod
    def reward_model(state):

        """
        This function defines the reward model R(s) of the MDP.

        Input
        -----
        state: int
            One of the states of the in the grid
            [0, ..., 15]

        """

        # only one reward
        if state == 15:
            return 1
        else:
            return 0

    def MDP(self, state, action):

        reward = self.reward_model(state)
        outputs  = self.transition_model(state, action)

        _output_list = []

        for output in outputs:
            _temp = list(output)
            _temp.insert(2, reward)

            _output_list.append(tuple(_temp))

        return _output_list

    def step(self, action):

        # get all possible outputs from MDP
        _output_list = self.MDP(self.state, action)
        num_outputs = len(_output_list)

        ## sample output based on probability
        # store all probs
        probs = []
        for _tuple in _output_list:
            probs.append(_tuple[0])

        # choose output
        idx = np.random.choice(num_outputs, p=probs)
        sample = _output_list[idx]
        _, next_state, reward, done = sample

        # update current state
        self.state = next_state

        return next_state, reward, done

    def reset(self):

        self.state = 0

        return self.state