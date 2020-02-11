
%% Copy and revise based on the fitness.m
fre = x;
path_cost_1 = (60/fre(2)) + 30 + (60/fre(4));
path_cost_2 = (60/fre(1)) + 5 + (60/fre(2)) + 25 + (60/(fre(4))) + 16;
path_cost_3 = (60/fre(3)) + 10 + (60/(fre(4))) + 16;
OD_cost_14 = min([path_cost_1,path_cost_2,path_cost_3]);
Pas_cost =  OD_cost_14 * 200;
Operation_cost = sum(fre) * 1000;

fprintf('Total Pas Cost = %s, Operator Cost = %s',Pas_cost,Operation_cost);