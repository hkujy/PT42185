"""
1. main proram code for the transit network assignment model 
"""

import input
from graph import graph_class
import lp

if __name__ == "__main__":

    graph = input.input_network()
    lp.model()
    
    pass
