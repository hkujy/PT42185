% The lower level assignment function 
% input: frequency 
% output: fitness value, which is the objective value solved by python 

function fitness = assignment(fre)
% get results 
res = py.lowerlp.assignment(fre);
% set fitness to be the objective value of the LP
fitness = res{'fun'};

x_sol = double(py.array.array('d',py.numpy.nditer(res{'x'})));

Flow_A_B = x_sol(1);
Flow_A_X2 = x_sol(2);
Flow_X2_Y =  x_sol(3);
Flow_Y_B = x_sol(4);
Flow_X2_X = x_sol(5);
Flow_X_Y3 = x_sol(6);
Flow_Y_Y3 = x_sol(7);
Flow_Y3_Y = x_sol(8);
Flow_Y3_B = x_sol(9);


return

