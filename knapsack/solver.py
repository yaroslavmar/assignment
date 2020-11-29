#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it_initial(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def solve_it_greedy(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    df = pd.DataFrame(items)
    df['density'] = df['value']/df['weight']
    df.sort_values('density', ascending = False, inplace = True)
    
    items2 = list(df.itertuples(name='Row', index=False))

    value = 0
    weight = 0
    taken = [0]*len(items2)

    for item in items2:
        if weight + item.weight <= capacity:
            taken[item.index] = 1   
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    DP_table = [[0 for _ in range(capacity+1)] for _ in range(item_count+1)]
    
    for j in range(item_count+1):
        for k in range(capacity+1):
            if j == 0 or k == 0:
                DP_table[j][k] = 0
            elif items[j-1].weight <= k:
                item_weight = items[j-1].weight
                item_value = items[j-1].value
                DP_table[j][k] = max(DP_table[max(j-1, 0)][k], item_value + DP_table[max(j-1, 0)][k-max(item_weight, 0)])
            else:
                DP_table[j][k] = DP_table[j-1][k]
    

    # obtained value
    obtained_value = DP_table[item_count][capacity]

    # get decision
    k = capacity 
    taken = [0]*len(items)
    for j in reversed(range(item_count+1)):
        if DP_table[j][k] != DP_table[j-1][k]:
            taken[j-1] = 1
            k = k - items[j-1].weight
            
    

    # prepare the solution in the specified output format
    output_data = str(obtained_value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        #print(solve_it_initial(input_data))
        #print(solve_it_greedy(input_data))
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
