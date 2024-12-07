'''
Author: Ting Feng Fan Ling
Date  : 10/23/2024
'''

'''
Running Notes:
1. Make sure Python 3.x version is installed.
2. Numpy library must be installed. You can install numpy from the command line using 'pip install numpy'.
3. This code is used to simulate the calculation of the optimal number of TwoPlus headphones to make. Run 'mean_simulations(up, rp, cost, simulations)',
Where:
-up: Unit cost per headset (e.g. $28.50)
-rp: The retail price of each headset (e.g. $150)
-cost: The cost of disposing of unsold headphones (e.g. $8.50)
-simulations: Number of simulations, used to get more stable results
4. Example: 
-calling 'mean_simulations(28.5, 150, 8.5, 30)' will run 30 simulations and output the average best number of builds.
'''
import numpy as np

def num_twoplus(up,rp,cost,num):

    #create a list of length 1000 and randomly generate demand instances from N(150,20) at each index.
    random_demand = np.random.normal(150,20,1000)

    #calculate the average profit
    profits = []
    for i in random_demand:

        #Yes or No for Tax?
        tax = np.random.choice([True, False], p=[0.5,0.5])

        if tax:
            new_cost = 17
        else:
            new_cost = cost

        sold = min(num, i)
        unsold = max(num - sold,0)
        profit = (sold*rp) - (num*up) - (unsold*new_cost)
        profits.append(profit)
    return np.mean(profits), np.std(profits)

#defined the function to find out maximum profit in range of quantity 0 to 230.
def optimal_quantity(up,rp,cost):

    quantity = 0

    #Make sure that even if we calculate a negative profit, it can still be updated to a value greater than negative infinity
    max_profit = -float('inf')

    for num in range(0, 230):
        mean_profit, std_profit = num_twoplus(up,rp,cost,num)
        if mean_profit > max_profit:
            max_profit = mean_profit
            quantity = num
    return quantity
    
#defined a function to calculate the avg quantity from the simulations
def mean_simulations(up,rp,cost,simulations):
    quantities = []
    for _ in range(simulations):
        optimal_qty = optimal_quantity(up,rp,cost)
        quantities.append(optimal_qty)
    final_qty = int(np.mean(quantities))

    print('After ' + str(simulations) + ' times simulations, ' 'the final average optimal quantity is ' + str(final_qty)  + '.')

mean_simulations(28.5,150,8.5,30)
