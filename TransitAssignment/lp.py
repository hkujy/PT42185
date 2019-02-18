"""
    This is for creating the Lp Problem 
    LP Model
        min CX
    Subject 
        Ax<=B
Accordingly, it contains three functions 
a. find matrix C
b. find matrix A and vector B
c. solve the model 
Remarks:
a. if you are using other package or method to solve LP, i.e., cCPLEX, there are different ways (probably simple) to add constraints and build the model.
Nevertheless, as long as you know how to create matrix A, B, C, you should be able to solve general LP problem.
"""

from graph import graph_class


def get_vector_C():
    """
    It contiains two part
    1. The first part is the [link cost]* link flow 
    2. The second part is [1]*waiting time variables at each with each node
    """
    C = []

    return C

def get_matrix_A_and_vector_B():
    """

    """
    A = []
    B = []
    return A, B

def model(network:graph_class):
    
    c=[]
    a=[]
    b=[]
    """
        create a, b, c matrix for the LP problem
    """
    pass

