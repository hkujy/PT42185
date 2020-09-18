"""
    the script is created to the test pymoo packages
    __author__= "Yu Jiang"
    __email__ = "yujiang@dtu.dk
    __status__ = "trial"
    http://pymoo.org/
"""

import numpy as np
from pymoo.model.problem import Problem  # Step 1: define problem
from pymoo.algorithms.nsga2 import NSGA2  # Step 2: define the algorithm
from pymoo.factory import get_sampling, get_crossover, get_mutation   #define the algorithm
from pymoo.factory import get_termination # define the termination criteria
from pymoo.optimize import minimize       # define problem

class MyProblem(Problem):
    def __init__(self):
        super().__init__(n_var=2,n_obj=2,n_constr=2,xl=np.array([-2,-2]),xu=np.array([2,2]))

    def _evaluate(self,X,out,*args,**kwards):
        f1 = X[:,0]**2 + X[:,1]**2
        f2 = (X[:,0]-1)**2 + X[:,1]**2 
        g1 = 2*(X[:, 0]-0.1) * (X[:, 0]-0.9) / 0.18
        g2 = -20*(X[:, 0]-0.4) * (X[:, 0]-0.6) / 4.8

        out["F"] = np.column_stack([f1,f2])
        out["G"] = np.column_stack([g1,g2])

    pass


# Step 1: define the problem
vectorized_problem = MyProblem()
# Step 2: define the algorithm
algorithm = NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)
# Step 3: define the termination criteria
termination = get_termination("n_gen", 40)

# Step 4: define the minimisation problem

res = minimize(vectorized_problem,
               algorithm,
               termination,
               seed=1,
               save_history=True,
               verbose=True)



