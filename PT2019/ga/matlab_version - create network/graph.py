"""
    graph class
"""

class bus_line_class():
    """
        bus line class
    """
    def __init__(self,name,id,fre):
        self.name = name
        self.id = id
        self.fre = fre
        self.stops = []
    pass
class node_class():
    """
        node class containing node attributes
    """
    def __init__(self, node_name, node_id):
        self.id = node_id
        self.name = node_name
        self.out_links = []
        self.in_links = []
        self.lines = []
        self.demand = 0
    pass
class link_class():
    """
        link class, containing link attributes
    """
    def __init__(self,link_name,link_id):
        self.id = link_id
        self.name = link_name
        self.tail_node = []  
        self.head_node = []
        self.cost = -1
        self.lines = []
        self.fre = -1.0
    pass
class graph_class():
    """
        Graph class combing link, node and bus lines
    """
    def __init__(self):
        self.links = []
        self.nodes = []
        self.lines = []
    pass

