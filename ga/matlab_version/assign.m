% The lower level assignment function 
% input: frequency 
% output: fitness value, which is the objective value solved by python 

function fitness = assign(fre)
% get results 
res = py.lowerlp.assignment(fre);
% set fitness to be the objective value of the LP
fitness = res{'fun'};

return

