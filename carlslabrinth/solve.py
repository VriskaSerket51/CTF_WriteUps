# !pip install quantecon
import numpy as np
from quantecon.markov import DiscreteDP

T = np.load("T.npy")
R = np.load("R.npy")

R = np.swapaxes(R, 0, 1)
T = np.swapaxes(T, 0, 1)

ddp = DiscreteDP(R, T, 0.99)
res = ddp.solve(method='policy_iteration')

print("".join(list(map(str, res.sigma))))