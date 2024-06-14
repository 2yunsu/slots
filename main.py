import matplotlib.pyplot as plt
import slots
from slots import MAB, MAB_sell
import pdb
import random
import numpy as np
import pdb

#random seed
random_seed = 0
# torch.manual_seed(random_seed)  # torch
# torch.cuda.manual_seed(random_seed)
# torch.cuda.manual_seed_all(random_seed)  # if use multi-GPU
np.random.seed(random_seed)  # numpy
random.seed(random_seed)  # random

# Test multiple strategies for the same bandit probabilities
probs = [0.8, 0.9, 0.4]

strategies = [{'strategy': 'eps_greedy', 'regret': [], 'regret_sell': [], 'sell': [], 'pull': [], 'root': [],
               'label': '$\epsilon$-greedy ($\epsilon$=0.1)'},
            #   {'strategy': 'softmax', 'regret': [], 'regret_sell': [],
            #    'label': 'Softmax ($T$=0.1)'},
            #   {'strategy': 'ucb', 'regret': [], 'regret_sell': [],
            #    'label': 'UCB1'},
            #   {'strategy': 'bayesian', 'regret': [], 'regret_sell': [],
            #    'label': 'Bayesian bandit'},
              ]

for s in strategies:
    s['mab'] = slots.MAB(probs=probs, live=False)

for s_sell in strategies:
    s_sell['mab_sell'] = slots.MAB_sell(probs=probs, live=False)

# Run trials and calculate the regret after each trial
for t in range(200):
        s['mab']._run(s['strategy'])
        s['regret'].append(s['mab'].regret())

for z in range(10):
    s_sell['mab_sell'].bandits.root = z+1
    s_sell['mab_sell'].pull_no = [0,0,0]
    s_sell['mab_sell'].sell_no = [0,0,0]
	for t in range(1000):
        for s_sell in strategies:
            s_sell['mab_sell']._run(s_sell['strategy'])
            s_sell['regret_sell'].append(s_sell['mab_sell'].regret())

    s_sell['sell'].append(np.sum(s_sell['mab_sell'].sell_no))
    s_sell['pull'].append(np.sum(s_sell['mab_sell'].pull_no))
    s_sell['root'].append(1/(z+1))
    print("root: ", 1/(z+1))
    print("pull_no / sell_no: ", np.sum(s_sell['mab_sell'].pull_no),  np.sum(s_sell['mab_sell'].sell_no))

for s in strategies:
    plt.plot(s['root'], s['sell'], label="Sell")
    plt.plot(s['root'], s['pull'], label="Pull")

# for s in strategies:
#     plt.plot(s['regret'], label="pull "+ s['label'])

# for s_sell in strategies:
#     plt.plot(s_sell['regret_sell'], label='sell '+ s['label'])

plt.legend()
plt.xlabel(r'$U_M$')
plt.ylabel('number of pulls/sells')
plt.title('Risk aversion tendency based on Marginal Utility')
plt.savefig('./graph/root_sell.png')
plt.clf()
