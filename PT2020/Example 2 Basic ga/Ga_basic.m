clear;clc;
rng default % For reproducibility
%% EXAMPLE 1
x = ga(@fitness,2); % solve function using GA
% display the fitness value
fprintf('simple case: fit = %d\n',fitness(x));
fprintf('simple case: x1 = %d, x2 = %d \n',x(1),x(2));
%% EXAMPLE 2 add constraints 
% set lower and upper bound
lb = [-10,5];
ub = [100,100];
x = ga(@fitness,2,[],[],[],[],lb,ub);
fprintf('add constraint: fit = %d\n',fitness(x));
fprintf('add constraint: x1 = %d, x2 = %d \n',x(1),x(2));
%% EXAMPLE 3 restirct taht x only binary value 
lb = [-10,0];
ub = [100,1];
x = ga(@fitness,2,[],[],[],[],lb,ub,[],(2));
fitness_value = fitness(x);
fprintf('restrict x2 is binary: fit = %d\n',fitness(x));
fprintf('restrict x2 is binary: x1 = %d, x2 = %d \n',x(1),x(2));

%% EXAMPLE 4 obtain and set ga options

opts = optimoptions('ga');
opts = optimoptions(opts,'MaxGenerations',100,'PopulationSize',100,'FunctionTolerance',0.001,'Display','final');
x = ga(@fitness,2,[],[],[],[],lb,ub,[],(2),opts);

%%

