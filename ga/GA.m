% reference 
% https://se.mathworks.com/help/gads/ga.html

clc;clear;
A =[];
b=[];
Aeq =[];
beq =[];
nonlcon=[];
lb = [3.0,3.0,3.0,3.0]; % lower bound of 
ub = [15.0,15.0,15.0,15.0];
nvars = 4;

rng default % For reproducibility generate random number
fun = @assignment;
opts = optimoptions(@ga,'PlotFcn',{@gaplotbestf});
opts = optimoptions(opts,'MaxGenerations',20,'PopulationSize',10,'FunctionTolerance',0.001,'Display','final');

%x = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,options)
fre_solution = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,opts);

%display the final lower level objective
py.lower_level.assignment(fre_solution)


