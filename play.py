# MIT License

# Copyright (c) 2017 Kim Jeong Ju

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
#!/usr/bin/env python
import sys
import os
import time
import click

from gym_tictactoe.env import TicTacToeEnv, agent_by_mark

from montecarlo import RolloutAgent

class HumanAgent(object):
    def __init__(self, mark):
        self.mark = mark
        self.agenttype = 'Human'

    def act(self, ava_actions):
        while True:
            # uloc = input("Enter location[1-9], q for quit: ")
            uloc = input("[1-9]: ")
            if uloc.lower() == 'q':
                return None
            try:
                action = int(uloc) - 1
                if action not in ava_actions:
                    raise ValueError()
            except ValueError:
                print("Illegal location: '{}'".format(uloc))
            else:
                break

        return action



@click.command(help="Play human agent.")
@click.option('-n', '--show-number', is_flag=True, default=False,
              show_default=True, help="Show location number in the board.")
def play(show_number):
    env = TicTacToeEnv(show_number=show_number)
    # print("101", env.available_actions())
    ROLLOUTS = 1000
    REWARD_FACTOR = 1 # because rollout agent is player 2
    agents = [HumanAgent('X'),
            #   HumanAgent('X')]
              RolloutAgent('O', ROLLOUTS, REWARD_FACTOR)]
    episode = 0
    while True:
        state = env.reset()
        _, mark = state
        done = False
        _ = os.system('clear')
        print('')
        env.render()
        while not done:
            agent = agent_by_mark(agents, mark)
            env.show_turn(True, mark)
            ava_actions = env.available_actions()
            if agent.agenttype == 'rollout':
                action = agent.act(ava_actions, env)
            else:
                action = agent.act(ava_actions)
            if action is None:
                sys.exit()

            state, reward, done, info = env.step(action)


            _ = os.system('clear')
            print('')
            env.render()
            if done:
                env.show_result(True, mark, reward)
                # print("Reward:", reward)
                break
            else:
                _, mark = state
        time.sleep(10)
        episode += 1


if __name__ == '__main__':
    play()
