"""
1. The function is adjusted from the main transit assignment model  
Remarks:
1. This code solves LP problem in 1989 paper using python
2. I created a graph class to faciliate building the Lp model. 
   For simplicity, you can just creat the A, B, C matrix directly
3. Becareful of inputing the netwok data, any mistake causes you get wrong results 
   or no results  
4. I hope the code is easy to follow 
"""

import os
import setinput 
from graph import graph_class
import lp


def assignment(fre):
    """
        input are the frequencies for the three lines
    """
#    if len(fre) != 4:
#        print("The number of input frequency is not 4")
#        os.system('pause')
#  step 1: input network 

    graph = setinput.readnetwork(fre)
#  step 2: solve model and out results on screen

    res = lp.model(graph)

    return res
    
