% Your first task is to finish compute cost for other OD pairs
function [fit] = Fitness(NetworkSol)

% NetworkSol refer to the frequency values
fre = NetworkSol;
% The lower level problem is to compute the total cost 
% Total cost = total pas cost + total operation cost

%% Compute total passenger cost
% I use OD pair 1 -> 4 as an example
% step 1: find the all possible path from 1 - 4 
%    path 1: 1->2->3(route 2)->tranfer -> 4 (route 4)
path_cost_1 = (60/fre(2)) + 30 + (60/fre(4));
%    path 2: 1->2 (route 1)->transfer -> 3 (route 2) -> 4 (route 4)
path_cost_2 = (60/fre(1)) + 5 + (60/fre(2)) + 25 + (60/(fre(4))) + 16;
%    path 3: 1 -> 3 (route 3) -> tranfer -> 4 (route 4)
path_cost_3 = (60/fre(3)) + 10 + (60/(fre(4))) + 16;
% step 2 : assume passenger use the shortest path 
OD_cost_14 = min([path_cost_1,path_cost_2,path_cost_3]);
Pas_cost =  OD_cost_14 * 200;
Operation_cost = sum(fre) * 1000;

fit = Pas_cost + Operation_cost;

