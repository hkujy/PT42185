clear;clc;
rng default % For reproducibility
%% EXAMPLE Simple Frequency Design using GA

%% Set Network
SetNet
%plot(G,'Layout','force','EdgeLabel',G.Edges.Weight);


%% Set GA parameters and run GA
%% set the boundary of the 4 frequency varaibles 
lb = [2.0,2.0,2.0,2.0];
ub = [12.0,12.0,12.0,12.0];

%% Set Parameters used in GA
opts = optimoptions('ga'); 
opts = optimoptions(opts,'MaxGenerations',20,'PopulationSize',20,'FunctionTolerance',0.001,'Display','final','PlotFcn', @gaplotbestf);
%% Solve GA
% x = ga(@Fitness,4,[],[],[],[],lb,ub,[],(1:4),opts);
x = ga(@Fitness,4,[],[],[],[],lb,ub,[],opts);
% x = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,options)
output




