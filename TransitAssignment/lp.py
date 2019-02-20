"""
    This is for creating the Lp Problem 
    LP Model
        min CX
    Subject 
        A_ub @ x <= b_ub
        A_eq @ x == b_eq
        lb <= x<=ub
Accordingly, it contains four functions 
a. find matrix C
b. find matrix A_ub, A_eq, vector b_ub, b_eq
c. find vector lb, ub for 
d. solve the model 
Remarks:

1. if you are using other package or method to solve LP, i.e., CPLEX, there are different ways (probably simple) to add constraints and build the model.
Nevertheless, as long as you know how to create matrix A, B, C, you should be able to solve general LP problem.

2. One important step is to ensure the coefficient is corresponding to the decsion variables


3. Dimension of C = Dimension of x = number of decision variables = number of links + number of nodes
4. Dimension of b_eq = number of nodes: flow conservation constraints at each node
5. Dimension of b_ub = number of links : flow distribution constraint
6. Dimension of A_ub = number of links * [number of links + number of nodes]
6. In our problem, there is 10 links. so variables index [0] - [9] represent the 10 link decsion variable. 
7. There are 6 nodes, so variables index [10] - [16] denote the waiting time variables at each node
"""

from graph import graph_class
from scipy.optimize import linprog


def get_vector_C(g:graph_class):
    """
        It contiains two part
        1. The first part is the coefficient for link variables 
        2. The second part is the coefficient for node variables, which is 1
    """
    C = []
    for l in g.links:
        C.append(l.cost) 
    for n in g.nodes:
        C.append(1)

    return C

def get_A_ub_and_B_ub(g:graph_class):
    """
     v_{a}*<=f*w_{i} is tranformed to v_{a} - f*w_{i} <=0
     v_{a} >=0
     -v_{a}<=0
     1. the first coefficient is for link {a}
     2. the secont coefficient is for node {i}, which is the tail node of link i
    """
    # demension of B_ub  = number of links
    B_ub = [0]*(2*len(g.links))
    A_ub = []
    for l in range(0,2*len(g.links)):
        A_ub.append([0]*(len(g.links) + len(g.nodes)))

    # set coefficients following the sequence of links
    row = 0
    for l in g.links:
        v_var_index = l.id
        w_var_index = l.tail_node[0].id + len(g.links)
        f_coefficient  = l.lines[0].fre
        A_ub[row][v_var_index] = 1
        A_ub[row][w_var_index] = -1*f_coefficient
        B_ub[row] = 0
        row =  row + 1
    for l in g.links:
        v_var_index = l.id
        A_ub[row][v_var_index] = -1
        B_ub[row] = 0
        row =  row + 1

    
    return A_ub, B_ub


def get_A_eq_and_B_eq(g:graph_class):
    """
        sum(out link flow)  - sum(in link flow)  = demand generated at each node i
    """ 
    # create matrix
    A_eq = []
    B_eq = [0]*len(g.nodes)
    for n in range(0, len(g.nodes)):
        A_eq.append([0]*(len(g.links) + len(g.nodes)))
    # build matrix following the sequence of links
    row = 0
    for n in g.nodes:
        for l in n.in_links:
            in_link_var_index = l.id
            A_eq[row][in_link_var_index] = -1
        for l in n.out_links:
            out_link_var_index = l.id
            A_eq[row][out_link_var_index] = 1
        if n.name =="A": 
            B_eq[row] = 1
        elif n.name =="B":
            # This is important, I forgot this first time
            B_eq[row] = -1  
        else:
            B_eq[row] = 0
        row = row + 1
    for row in A_eq:
        print(row)
    print(B_eq)
    return A_eq, B_eq
    pass

def get_lb_and_ub(g:graph_class):
    """
        get the upper and lower bound value for x value
        for simplicity, I set the lower bound to be 0 and upper bound to 100
        the lower and upper bound value could set tight
    """
    lb = [0] * (len(g.links)+len(g.nodes))
    ub = [100] * (len(g.links) +len(g.nodes))
    bounds =[]
    for i in range(0, len(lb)):
        bounds.append((lb[i],ub[i]))
        
    # print(bounds)

    return lb, ub, bounds
    pass

def model(network:graph_class):
    
    """
        create a, b, c matrix for the LP problem
    """
    C = get_vector_C(network)
    (A_ub, B_ub) = get_A_ub_and_B_ub(network)
    (A_eq, B_eq) = get_A_eq_and_B_eq(network)
    (lb, ub, bounds) = get_lb_and_ub(network) 
    with open("print_model.csv","w+") as f:
        pass
    res = linprog(C,A_ub=A_ub,b_ub=B_ub,A_eq=A_eq,b_eq=B_eq, bounds=bounds)



    print(res)


