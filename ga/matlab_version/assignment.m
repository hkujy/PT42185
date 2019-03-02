% The lower level assignment function 
% input: frequency 
% output: fitness value, which is the objective value solved by python 

function fitness = assignment(fre)
% get results 
res = py.lower_level.assignment(fre);
% set fitness to be the objective value of the LP
fitness = res{'fun'};

return

