"""
    python code for the msa 
    course PT42185
"""
import networkx as nx   ## network package
import math

demand = 500
theta = 0.1
walk_link_cap = 9999999999 # very large capacity for the walking link

def set_network():
    # create a network 
    graph = nx.DiGraph()
    # add nodes
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('O')
    graph.add_node('D')

    # add edges, and set initial flow =0
    graph.add_edge('O','A',t0=4,cap=100,v=0,weight=0)
    graph.add_edge('O','B',t0=25,cap=walk_link_cap,v=0,weight=0)
    graph.add_edge('A','B',t0=5,cap=walk_link_cap,v=0,weight=0)
    graph.add_edge('A','D',t0=25,cap=200,v=0,weight=0)
    graph.add_edge('B','D',t0=5,cap=500,v=0,weight=0)
    # path = nx.shortest_path(graph, 'O', weight = 't0')

    path = set_path_set()
    print(path)
    return graph
    pass

def set_path_set():
    paths=[]
    temp_path = path_class()
    temp_path.links.append(('O','B'))
    temp_path.links.append(('B','D'))
    paths.append(temp_path)
    temp_path = path_class()
    temp_path.links.append(('O','A'))
    temp_path.links.append(('A','D'))
    paths.append(temp_path)
    temp_path = path_class()
    temp_path.links.append(('O','A')) 
    temp_path.links.append(('A','B')) 
    temp_path.links.append(('B','D')) 
    paths.append(temp_path)
    return paths

def MSA():
    """
        msa method for the assignment
    """
    #set default paramters values
    maximum_iter = 100
    acceptable_gap = 0.001
    gap = 100  ## initial gap value
    # step 0: read network 
    my_graph=my_network_class(set_network())
    my_graph.update_edge_cost() # get initial edge cost
    my_graph.paths = set_path_set() # define path set

    # Step 1: set initial flow
    I = 1 # Iteration counter or stepsize 
    x = [demand/len(my_graph.paths)]*len(my_graph.paths) # create initial path flow

    while I < maximum_iter and gap > acceptable_gap:
    # Step 2: update path flow 
        my_graph.update_path_flow(x)
        # update edge flow and cost
        my_graph.update_edge_flow()
        my_graph.update_path_cost()
        # update path prob
        my_graph.update_path_prob()
    # Step 3: compute Y flow based on the logit prob
        y = []
        for p in my_graph.paths:
            y.append(demand*p.logit_prob)

    # Step 4: Update x flow for the next iteration based on MSA updating method
        for i in range(0, len(x)):
            x[i] = x[i] + 1/I*(y[i]-x[i])
    # Step 5: check the convergence, which is the maximum abs difference between the two prob values
        gap = max([abs(my_graph.paths[p].prob-my_graph.paths[p].logit_prob) for p in range(0, len(my_graph.paths))])
        print('Iteration = {0}, gap = {1}'.format(I,gap))

        I+=1
    # print final solution
    print("*********Final Solution**********")
    print("PathID,Flow,Cost,Prob,Logit_Prob") 
    for p in range(0, len(my_graph.paths)):
        print("{0},{1:.2f},{2:.2f},{3:.2f},{4:.2f}".format(p,my_graph.paths[p].flow,my_graph.paths[p].cost,my_graph.paths[p].prob,my_graph.paths[p].logit_prob))
    pass


if __name__ == "__main__":

    MSA()
    
    pass

