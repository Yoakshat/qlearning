import froglily
import random
import numpy as np

N = 100

# enforce you can only go forward
# just when you're selecting best action, don't make it possible

# 1 to 99 steps 
# (N) states x (N-1) actions

qtable = np.zeros((N, N-1))
obs = [N,1]
disc = 0.9
lr = 0.01

# build the qtable by starting at state (N-1) and trying all actions
# then go backward till state 1

for state in range(N-1, 1, -1): 
    obs[1] = state

    # then take all actions possible
    # to know an action's expected value, run multiple simulation

    for sim in range(100): 
        for action in range(1, 1 + (obs[0] - obs[1])): 

            newObs, reward, terminated, _ = froglily.take_action(obs, action)
            newState = newObs[1]

            # update qtable for respective state and reward
            qtable[state-1][action-1] += lr * (reward + disc * np.max(qtable[newState-1]) 
                                            - qtable[state-1][action-1])

# print(qtable)

# based on q-table and actually possible actions pick best action


    
