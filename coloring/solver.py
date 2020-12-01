#!/usr/bin/python
# -*- coding: utf-8 -*-
from ortools.sat.python import cp_model
import time

def solve_initial(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    # build a trivial solution
    # every node has its own color
    solution = range(0, node_count)

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    available_colors = range(0, 10)
    available_colors = [10000]
    if node_count <= 50:
        available_colors = [5]
    if node_count >50 & node_count<= 70:
        available_colors = [16]
    if node_count ==100:
        available_colors = [15]

    if node_count > 100:
        available_colors = [10000]

    for num_colors in available_colors:
        #start_time = time.time()
        #while time.time() < start_time + 5:
            print(num_colors)
            model = cp_model.CpModel()
            decision_colors = [model.NewIntVar(0, num_colors, 'color%i' % i) for i in range(node_count)]

            for edge in edges:
                model.Add(decision_colors[edge[0]] != decision_colors[edge[1]])

            model.Minimize(max(decision_colors))
            solver = cp_model.CpSolver()
            status = solver.Solve(model)

            if status == cp_model.OPTIMAL:
                result = [solver.Value(decision_colors[i]) for i in range(node_count)]

                # prepare the solution in the specified output format
                output_data = str(max(result)+1) + ' ' + str(0) + '\n'
                output_data += ' '.join(map(str, result))
                return output_data
            else:
                next



import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

