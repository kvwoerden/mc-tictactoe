# MIT License

# Copyright (c) 2021 Koenraad van Woerden

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
import copy
import statistics
from collections import defaultdict


class RolloutAgent(object):
    def __init__(self, mark, rollouts, reward_factor):
        """A Monte Carlo rollout Tic Tac Toe agent

        Args:
            mark (string): agent mark ('O' or 'X')
            rollouts (int): number of rollouts per move to use
            reward_factor (int): +1 if the agent is the first player, -1 if
                 the agent is the second player
        """
        self.mark = mark
        self.agenttype = 'rollout'
        self.rollouts = rollouts
        self.reward_factor = reward_factor  # 1 if first player, -1 if second player

    def act(self, ava_actions, env):
        """Decide a move by doing Monte Carlo rollouts

        Args:
            ava_actions (list): available actions
            env (TicTacToeEnv): the current Tic Tic Toe environment

        Returns:
            int: integer describing the best action
        """
        results = defaultdict(list)
        for action in ava_actions:
            action_env = copy.deepcopy(env)
            _, reward, done_state, _ = action_env.step(action)
            for _ in range(self.rollouts):
                done = done_state
                # Make a deep copy so that we don't modify the original
                # environment:
                rollout_env = copy.deepcopy(action_env)
                while not done:
                    # Take random actions until the game ends
                    random_action = random.choice(
                        rollout_env.available_actions())
                    _, reward, done, _ = rollout_env.step(random_action)
                results[action].append(self.reward_factor * reward)
        averages = {k: statistics.mean(v) for k, v in results.items()}
        best = max(averages, key=averages.get)
        return best
