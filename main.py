import h5py 

import h5py
f1 = h5py.File('task_data.hdf5', 'r')



import networkx as nx
import matplotlib.pyplot as plt
import random

my_graph = nx.Graph()





# TODO: make it better
some_hours = ['hour_1', 'hour_2']

graphs =[]


# def label_with_generation(gens, graph): 
#     gens_labels = { i[0]: i[1] for i in gens }
#     nx.draw_

# TODO: refactor
# TODO: only two graphs
# for i in some_hours: 
#     graph = nx.Graph()
#     pos = nx.spring_layout(graph)
#     for j in f1['results'][i]['branches'][:]:
#         graph.add_node(j[0], Position=(random.randrange(0, 100), random.randrange(0, 100)))
#         graph.add_node(j[1], Position=(random.randrange(0, 100), random.randrange(0, 100)))
#         graph.add_edge(j[0], j[1], weight=j[2])
#     # i[1]
#     gens_labels = { i[0]: i[1] for i in f1['results'][i]['gens'][:, 0:2] }
#     costs = f1['results'][i]['nodes']
#     # all_labels = {i[0]: (i[]) }
#     nx.draw(graph, pos=nx.get_node_attributes(graph, 'Position'), labels=gens_labels)
#     graphs.append(graph)
#     plt.pause(2)
#     exit(1)

# for i in graphs: 
#     plt.clf()
#     nx.draw(i, pos=nx.get_node_attributes(i, 'Position'))
#     plt.pause(0.5)

# while(True): 
#     for i in graphs: 
#         plt.clf()
#         nx.draw(i, pos=nx.get_node_attributes(i, 'Position'))
#         plt.pause(0.5)





# result = {i[0]: i[1] for i in some_data}

## TODO: new begining

# Build basic graph 

# detect changes in direction and visualize them


# I assume the nodes are the same in every graph
# compute the difference in wages
import numpy as np

PURPLE = '#db2ffe'
YELLOW = '#feed2f'
GRAY = '#979795'

first_hour_edges = np.array(f1['results']['hour_1']['branches'][:, 2:3]).flatten()
second_hour_edges = np.array(f1['results']['hour_2']['branches'][:, 2:3]).flatten()
edge_direction_array = np.multiply(first_hour_edges, second_hour_edges) > 0
edges = np.array(f1['results']['hour_1']['branches'][:, 0:2])
original_graph_directions = f1['results']['hour_1']['branches'][:, 2] > 0
edges = np.array([np.flip(i) if original_graph_directions[idx]<0 else i for idx, i in enumerate(edges)])
nodes = np.unique(np.array(edges).flatten())
edge_labels_showing_flow_absolute_diff = np.round(np.abs(np.array(f1['results']['hour_1']['branches'][:, 2]) - np.array(f1['results']['hour_2']['branches'][:, 2])))

hour_1_genes = np.array(f1['results']['hour_1']['gens'][:, 0:2])
hour_2_genes = np.array(f1['results']['hour_2']['gens'][:, 0:2])

hour_1_genes_dict = dict(zip(hour_1_genes[:, 0], hour_1_genes[:,1]))
hour_2_genes_dict = dict(zip(hour_2_genes[:, 0], hour_2_genes[:,1]))

for i in nodes: 
    if i not in hour_1_genes_dict: 
        hour_1_genes_dict[i] = 0
    if i not in hour_2_genes_dict: 
        hour_2_genes_dict[i] = 0

genes_hour_1 = np.array([[i, hour_1_genes_dict[i]] for i in hour_1_genes_dict])
genes_hour_2 = np.array([[i, hour_2_genes_dict[i]] for i in hour_2_genes_dict])

generation_hour_1_types = genes_hour_1[:,1] - np.array(f1['results']['hour_1']['nodes'][:, 2])
generation_hour_2_types = genes_hour_2[:,1] - np.array(f1['results']['hour_1']['nodes'][:, 2])

node_types_hour_1 = np.array([2 if i > 0 else 1 for i in generation_hour_1_types])
node_types_hour_2 = np.array([2 if i >= 0 else 1 for i in generation_hour_2_types]) # TODO: just a dummy example
type_changes = []
for i in (node_types_hour_1 - node_types_hour_2):
    if i == -1:
        type_changes.append(PURPLE)
    elif i == 1:
        type_changes.append(YELLOW)
    else:
        type_changes.append(GRAY)

for _ in range(5):
    print('&&&')
print(type_changes)

# 1->2 
# Is generator
# print(node_types_hour_1 - node_types_hour_2)


# print(node_types_hour_1)
# # for i in range(1, 25): 
# #     print(f1['results']["hour_"+str(i)]['nodes'][:, 1])
# #     for _ in range(5):
# #         print("---------")
# print(node_types_hour_2)

# if gen - demand > 0:
#     generator 
# else: slave



###########################33
# Assuming Type 2 is Generator type 1 is slave
#######################
# for i in range(1, 25):
#     print(np.array(f1['results']['hour_1']['nodes'][:, 1]) - np.array(f1['results']["hour_" + str(i)]['nodes'][:, 1]))
# nodes_types_diff = np.array(f1['results']['hour_1']['nodes'][:, 1]) - np.array(f1['results']['hour_2']['nodes'][:, 1])
# print(nodes_types_diff)
# hour_1_node_energy = np.array(f1['results']['hour_1']['nodes'][:, 2]) - np.array(f1['results']['hour_1']['gens'][:, 1])
# hour_2_node_energy = 
# difference_in_erergy = 
# 'y' -> Generator - -> +
# 'b' -> slave + -> -

# demand - genes
# < takes energy 
# < generates energy



# build graph to visualize 
graph = nx.DiGraph() 

for node in nodes: 
    graph.add_node(node)

edge_labels = np.array([])
# Add edges
for idx, edge in enumerate(edges):
    edge_color = 'green' if edge_direction_array[idx] else 'black'
    edge_directed = edge if not(edge_direction_array[idx]) else np.flip(edge)
    edge_weight = edge_labels_showing_flow_absolute_diff[idx]
    edge_args = { 'color': edge_color, 'weight': edge_weight } if edge_weight > 0 else { 'color': edge_color }
    graph.add_edge(edge_directed[0], edge_directed[1], **edge_args)

edge_colors = nx.get_edge_attributes(graph,'color').values()
weight_labels = nx.get_edge_attributes(graph,'weight')

pos = nx.kamada_kawai_layout(graph)
from matplotlib.lines import Line2D

legend_elements = [
    Line2D([0], [0], marker='_', linewidth='2.0', color='g', label='Flow direction change',markerfacecolor='g', markersize=15), 
    Line2D([0], [0], marker='o', color='w', label='Node is now a generator',markerfacecolor=PURPLE, markersize=15), 
    Line2D([0], [0], marker='o', color='w', label='Node now is slave',markerfacecolor=YELLOW, markersize=15), 
]

plt.figure(3,figsize=(12,12))
nx.draw(graph, pos, edge_color = edge_colors, with_labels=True, node_color=type_changes)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=weight_labels)

# Show legend for the graph
plt.legend(handles=legend_elements, loc='upper right')
plt.show()


for _ in range(25):
    print("---------")

print(nx.cytoscape_data(graph)['elements'])

for _ in range(25): 
    print("END------")

print(nx.cytoscape_data(graph)['elements']['edges'])

for _ in range(30):
    print("siema siema sieam")

print(nx.cytoscape_data(graph))
elo = input("end?")
