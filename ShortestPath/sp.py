"""
Reference 
https://networkx.github.io/documentation/stable/tutorial.html

1. Ths code finds the shortest path using the network shown in the class ppt
2. Through this toy example, you can play with the networkX package
3. There should be shortest path package or lib in other programming language 
4. For our course, it is not required for you to learn to code your own shortest path
5. However, as a student learning transportation, know how to find shortest paht is a core competences. You will need it almost everywhere.
"""
import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
# create directed graph
G = nx.DiGraph()
# add nodes of the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
# add links of the graph
G.add_edge('A','B', weight = 4 )
G.add_edge('A','C', weight = 1)
G.add_edge('C','B', weight = 2)
G.add_edge('C','D', weight = 2)
G.add_edge('B','E', weight = 3)
G.add_edge('D','E', weight = 3)
# there are other ways adding nodes and edges you can check it online
# find the shortest path 

pred, dist = nx.dijkstra_predecessor_and_distance(G, 'A')
print("The pred for each node with respect to source A")
print(sorted(pred.items()))
print("The distance label for each node with respect to A")
print(sorted(dist.items()))
print("The shrotest path between A and E is")

# print shortest path between a pair of nodes
print(nx.dijkstra_path(G, 'A', 'E'))