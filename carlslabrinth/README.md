# CaRLsLabrinth

With Markov Decision Process(MDP), you have to calculate the Policy.

MDP is for Reinforcement Learning, you can search it at wikipedia for detail.

Anyway, in pip, there is the package `quantecon` which helps you to solve mdp.

First, do `pip install quantecon`.

Then, run the python program.
```python
import numpy as np
from quantecon.markov import DiscreteDP

T = np.load("T.npy")
R = np.load("R.npy")

R = np.swapaxes(R, 0, 1)
T = np.swapaxes(T, 0, 1)

ddp = DiscreteDP(R, T, 0.99)
res = ddp.solve(method='policy_iteration')

print("".join(list(map(str, res.sigma))))
```

Send the policy to server, then you can get the flag.

Flag: **TUCFT{Congr@ts_onthe@PP!3_pi}**