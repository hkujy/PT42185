"""
1. main program code for the transit network assignment model 

Remarks:
1. This code solves LP problem in 1989 paper using python
2. I created a graph class to faciliate building the Lp model. 
   For simplicity, you can just creat the A, B, C matrix directly
3. Becareful of inputing the netwok data, any mistake causes you get wrong results 
   or no results  
4. I hope the code is easy to follow 

"""

import input
from graph import graph_class
import lp

if __name__ == "__main__":

#  step 1: input network 
    graph = input.input_network()
#  step 2: solve model and out results on screen
    lp.model(graph)
    pass
