# Tic Tac Toe with Monte Carlo rollout agent

This implements an agent playing Tic Tac Toe using Monte Carlo Rollout as described in section 8.10 of Sutton-Barto. The agent is implemented in `montecarlo.py`.

The package [gym-tictactoe](https://github.com/haje01/gym-tictactoe) is used as a Tic Tac Toe environment, and the example [human agent](https://github.com/haje01/gym-tictactoe/blob/master/examples/human_agent.py) is used in `play.py` for the main game loop as well as for the player controls.

# How to run

To run, first install the dependencies in `requirements.txt`, for example using a pip in a virtual environment:

```bash
	$ python3 -m venv env
	$ source env/bin/activate
	$ pip install -r requirements.txt
```

Next, start the game as follows:

```bash
	$ python play.py
```

# How to play

The Monte Carlo agent makes the first move, and plays with the symbol `O`. After the agent made the first move, your console will look like this:

```
   | |
  -----
   |O|
  -----
   | |

X's turn.
[1-9]:
```

Pick a number from 1-9 to make a move, where the numbers correspond to the following moves:

```
  1|2|3
  -----
  4|5|6
  -----
  7|8|9
```

So for instance

```
   | |
  -----
   |O|
  -----
   | |

X's turn.
[1-9]: 3
```

might result in:

```
   | |X
  -----
   |O|O
  -----
   | |

X's turn.
[1-9]:
```
