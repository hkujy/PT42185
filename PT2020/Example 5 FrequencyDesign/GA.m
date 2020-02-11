
%%Step 1: try python in matlab 

py.print('Hello Word')

%%Step 1: try python in matlab 
%****************************
% you need to python scipy package is install 
% python -m pip install scipy
%********************************
%%

% reference 
% https://se.mathworks.com/help/gads/ga.html
%%%%%%%%% This it he main GA program of matlab
clc;clear;clearAllMemoizedCaches;

% set python version and dir location
% pyversion 'C:\Users\yujiang\AppData\Local\Programs\Python\Python37\python.exe'
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


fre=[4 4 4 4];
val = assignment(fre);

rng default % For reproducibility generate random number
fun = @assignment; % define fitness function
% set options used in GA
opts = optimoptions(@ga); % get options
opts = optimoptions(opts,'MaxGenerations',50,'PopulationSize',10,'FunctionTolerance',0.01,'Display','final','PlotFcn',{@gaplotbestf});

%x = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,options) this is default ga function in matlab
fre_solution = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,opts);
disp(fre_solution);
%display the final lower level objective use the final solution obtained from GA
py.lowerlp.assignment(fre_solution)


