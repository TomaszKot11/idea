from random import randrange
import h5py
import networkx as nx
import matplotlib.pyplot as plt
import random
from sklearn.cluster import KMeans
import numpy as np
from constants import PURPLE, YELLOW, GRAY, HDF5_DATA

# TODO: with could be better & more efficient
f1 = h5py.File(HDF5_DATA, 'r')

def prepare_graph(first_data = 'hour_1', second_data = 'hour_2'):
    '''
    Returns the Cytospace.js formatted data visualizing the difference between the 
    network in two snapshots
            Parameters:
                    first_data  (str): Name of first snapshot data
                    second_data (str): Name of second snapshot data

            Returns:
                    graph_cytospace_data (dict): Cytospace.js dictionary (JSON) for Dash
    '''
    first_hour_edges = np.array(f1['results'][first_data]['branches'][:, 2:3]).flatten()
    second_hour_edges = np.array(f1['results'][second_data]['branches'][:, 2:3]).flatten()

    edge_direction_array = np.multiply(first_hour_edges, second_hour_edges) > 0
    
    edges = np.array(f1['results'][first_data]['branches'][:, 0:2])
    original_graph_directions = f1['results'][first_data]['branches'][:, 2] > 0
    edges = np.array([np.flip(i) if original_graph_directions[idx]<0 else i for idx, i in enumerate(edges)])
    nodes = np.unique(np.array(edges).flatten())
    edge_labels_showing_flow_absolute_diff = np.round(np.abs(np.array(f1['results'][first_data]['branches'][:, 2]) - np.array(f1['results'][second_data]['branches'][:, 2])))

    hour_1_genes = np.array(f1['results'][first_data]['gens'][:, 0:2])
    hour_2_genes = np.array(f1['results'][second_data]['gens'][:, 0:2])

    # TODO: group multiple generators as in Email - they are unique in the dataset here (?)

    hour_1_genes_dict = dict(zip(hour_1_genes[:, 0], hour_1_genes[:,1]))
    hour_2_genes_dict = dict(zip(hour_2_genes[:, 0], hour_2_genes[:,1]))

    # TODO: refactor
    for i in nodes: 
        if i not in hour_1_genes_dict: 
            hour_1_genes_dict[i] = 0
        if i not in hour_2_genes_dict: 
            hour_2_genes_dict[i] = 0

    genes_hour_1 = np.array([[i, hour_1_genes_dict[i]] for i in hour_1_genes_dict])
    genes_hour_2 = np.array([[i, hour_2_genes_dict[i]] for i in hour_2_genes_dict])

    generation_hour_1_types = genes_hour_1[:,1] - np.array(f1['results'][first_data]['nodes'][:, 2])
    generation_hour_2_types = genes_hour_2[:,1] - np.array(f1['results'][second_data]['nodes'][:, 2])

    node_types_hour_1 = np.array([2 if i > 0 else 1 for i in generation_hour_1_types])
    node_types_hour_2 = np.array([2 if i > 0 else 1 for i in generation_hour_2_types])
    
    type_changes = []
    # TODO: refactor
    for i in (node_types_hour_1 - node_types_hour_2):
        if i == -1:
            type_changes.append(PURPLE)
        elif i == 1:
            type_changes.append(YELLOW)
        else:
            type_changes.append(GRAY)

    # build graph to visualize 
    graph = nx.DiGraph() 

    for idx, node in enumerate(nodes): 
        graph.add_node(node, color=type_changes[idx])

    # Add edges
    for idx, edge in enumerate(edges):
        edge_color = 'green' if edge_direction_array[idx] else 'gray'
        edge_directed = edge if not(edge_direction_array[idx]) else np.flip(edge)
        edge_weight = edge_labels_showing_flow_absolute_diff[idx]
        edge_args = { 'color': edge_color, 'weight': edge_weight } if edge_weight > 0 else { 'color': edge_color }
        graph.add_edge(str(edge_directed[0]), str(edge_directed[1]), **edge_args)

    return nx.cytoscape_data(graph)

# TODO: refactor code duplicate
def cluster_graph(no_groups, hour_two = 'hour_2'):
    '''
    Using KMeans clustering divides the flows of edges
            Parameters:
                    no_groups   (int): number of clusters
                    hour_two   (str): Name of the snapshot data
            Returns:
                    graph_cytospace_data (dict): Cytospace.js dictionary (JSON) for Dash
    '''
    graph = nx.DiGraph()
    edges = np.array(f1['results'][hour_two]['branches'][:, 0:2])
    original_graph_directions = f1['results'][hour_two]['branches'][:, 2] > 0
    edges = np.array([np.flip(i) if original_graph_directions[idx]<0 else i for idx, i in enumerate(edges)])
    nodes = np.unique(np.array(edges).flatten())
    weights = [[abs(i)] for idx, i in enumerate(np.array(f1['results'][hour_two]['branches'][:, 2:3]).flatten())] # TODO: optimize

    # K-means
    k_means = KMeans(n_clusters=no_groups, random_state=0)
    k_means_model_labels = k_means.fit(weights).labels_

    color_dict = {}
    for label in list(np.arange(no_groups)): 
        color_dict[label] = _random_hex_color() # TODO: make generation better

    edge_colors = list(map(lambda x: color_dict[x], k_means_model_labels))

    for idx, node in enumerate(nodes):
        graph.add_node(node, color=GRAY)

    for idx, edge in enumerate(edges):
        edge_args = {'color': edge_colors[idx], 'weight': round(weights[idx][0], MEGA_DEC)}
        graph.add_edge(str(edge[0]), str(edge[1]), **edge_args)

    return nx.cytoscape_data(graph)


#TODO: read_edgelist?
def _random_hex_color():
    '''Dummy method for random HEX color generation'''
    return '#' + str(hex(random.randint(0,16777215)))[2:]