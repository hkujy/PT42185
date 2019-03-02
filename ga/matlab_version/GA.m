% reference 
% https://se.mathworks.com/help/gads/ga.html
%%%%%%%%% This it he main GA program of matlab
clc;clear;
% step 1: set values based on the matlab instruction
A =[];
b=[];
Aeq =[];
beq =[];
nonlcon=[];
% upper and lower bound of the frequency
nvars = 4; % number of decision variables
lb = [3.0,3.0,3.0,3.0]; % lower bound 
ub = [15.0,15.0,15.0,15.0]; % upper bound

rng default % For reproducibility generate random number
fun = @assignment; % define fitness function
% set options used in GA
opts = optimoptions(@ga,'PlotFcn',{@gaplotbestf}); % plot output
opts = optimoptions(opts,'MaxGenerations',20,'PopulationSize',10,'FunctionTolerance',0.001,'Display','final');

%x = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,options) this is default ga function in matlab
fre_solution = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,opts);

%display the final lower level objective use the final solution obtained from GA
py.lower_level.assignment(fre_solution)


