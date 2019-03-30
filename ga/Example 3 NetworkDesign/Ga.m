clear;clc;
rng default % For reproducibility
%% EXAMPLE Simple Netwok Design using GA
s = [1 2 1 3 1 4 2 3 2 4 3 4];
t = [2 1 3 1 4 1 3 2 4 2 4 3];
weights = [5 5 2 2 4 4 6 6 4 4 1 1];
names = {'A','B','C','D'};
G = digraph(s,t,weights,names);
%plot(G,'Layout','force','EdgeLabel',G.Edges.Weight);
% Now select four links to build a transit network such that the travel
% time for A-C, A-B, A-D is minimum 

%% Set GA parameters and run GA
% There totally 12 links 
% a simple way is that there four decsion variables
% each variable represent a number between 1 - 12

lb = [1,1,1,1];
ub = [12,12,12,12];

opts = optimoptions('ga');
opts = optimoptions(opts,'MaxGenerations',100,'PopulationSize',20,'FunctionTolerance',0.001,'Display','final');
x = ga(@Fitness,4,[],[],[],[],lb,ub,[],(1:4),opts);
`




