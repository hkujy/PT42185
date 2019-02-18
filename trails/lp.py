from scipy.optimize import linprog


C = [-1,4]
A =[[-3,1],[1,2]]
B = [6,4]
x0_bound =[None, None]
x1_bound =[-3, None]

res = linprog(C, A_ub=A, b_ub=B,bounds=(x0_bound,x1_bound),options={"disp": True})
print(res)
print(res.fun)