function fitness = assignment(fre)

res = py.lower_level.assignment(fre);
fitness = res{'fun'};


return

