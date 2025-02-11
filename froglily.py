# newly invented frog lilypad game

import random

DECAY_LILIES = False
frog_position = 1

num_lilies = 100

decays = []

for _ in range(num_lilies): 
    decays.append(0.75 + 0.25 * random.random())

def yes(prob): 
    if random.random() < prob: 
        return True
    
    return False

# return reward, terminated (reward = numJumps/(how much there is left))
def take_action(obs, numJumps): 
    num_lilies = obs[0]
    frog_position = obs[1]

    new_obs = []

    terminated = False
    win = False

    reward = 0
    steps_left = num_lilies - frog_position

    # subtract some epsilon so it's possible to win!
    goBack = (numJumps / steps_left) - 0.05
    goForward = (1 - goBack)

    # with probability adjust
    if yes(goForward): 
        frog_position += numJumps
    else: 
        frog_position -= numJumps


    if(frog_position >= num_lilies):
        # you won!
        terminated = True
        win = True
        reward += 5
    elif(frog_position < 1): 
        # you lost
        terminated = True
        reward -= 5
    else:
        if DECAY_LILIES: 
            while True: 
                if yes(1 - decays[frog_position]):
                    # move frog position one back
                    frog_position -= 1
                    num_lilies -= 1
                    del decays[frog_position]
                else: 
                    decays[frog_position] *= 0.5
                    break

        # newStepsLeft = num_lilies - frog_position
        # reward += (steps_left - newStepsLeft)/steps_left

    new_obs.append(num_lilies)
    new_obs.append(frog_position)
    # also return observation ([num_lilies, frog_position])
    return new_obs, reward, terminated, win

# build a probability simulation
# how many times do you win out of 1000: 76/1000

# run simulation: create choose_action method
'''
wins = 0
for sims in range(1000): 
    # starting number
    obs = [num_lilies, frog_position]
    print(obs)

    while True: 
        # num_lilies and frog position changes
        obs, _, term, win = take_action(obs, 1 + (int)(random.random() * (obs[0] - obs[1])))
        print(obs[1])

        if term: 
            if win:
                wins += 1
            break

print("Wins: " +  str(wins) + "/1000")
'''
    







# randomly pick jump between 0


