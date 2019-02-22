"""
1. main proram code for the transit network assignment model 

Remarks:
1. the algorithm does not consider multiple OD pairs
"""

import input
from graph import graph_class
import lp

def test_matlab():
    print("connect to python")


if __name__ == "__main__":

    graph = input.input_network()
    lp.model(graph)
    test_matlab()
    pass
