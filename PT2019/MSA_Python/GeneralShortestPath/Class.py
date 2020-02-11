"""
    contains the class data
"""
import networkx as nx
class path_class():
    """
        path class
    """
    def __init__(self):
        self.flow = 0
        self.cost = 0
        self.links =[]
        self.logit_prob = 0 # probability computed via the logit formula
        self.prob = 0      # probability computed by flow/demand

    def get_cost(self,_graph:nx.DiGraph):
        """
            get path cost
        """
        self.cost=0
        for e in self.links:
            self.cost=self.cost+_graph.edges[e]['weight']

class my_network_class():
    """
        my network class
    """
    def __init__(self, _graph):
        self.graph =_graph
        self.paths = []

    def update_edge_flow(self):
        """
            compute link flow from path flow
        """
        for e in self.graph.edges.items():
            e[1]['v'] = 0
        for p in self.paths:
            for l in range(0, len(p.links)):
                self.graph.edges[p.links[l]]['v']+=p.flow

    def update_edge_cost(self):
        """
            compute link cost given link flow
            this is a BPR type function 
            cost = t0 + v/cap
        """
        for e in  self.graph.edges.items():
            e[1]['weight']=e[1]['t0']+e[1]['v']/e[1]['cap']

    def update_path_cost(self): 
        """
            compute path cost using the updated edge cost
        """
        self.update_edge_cost()
        for p in self.paths:
            p.get_cost(self.graph)

    def update_path_prob(self):
        """
            compute path probability, using both logit and flow/demand 
        """
        path_exp = []
        for p in self.paths:
            path_exp.append(math.exp(-theta*p.cost))
        for p in range(0,len(self.paths)):
            self.paths[p].logit_prob = path_exp[p]/sum(path_exp)
            self.paths[p].prob = self.paths[p].flow/demand

    def update_path_flow(self,_path_flow):
        """
            update path flow
        """
        for p in range(0, len(self.paths)):
            self.paths[p].flow =  _path_flow[p]