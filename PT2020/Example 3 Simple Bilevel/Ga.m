clear;clc;
rng default % For reproducibility
%% EXAMPLE
x1 = ga(@UpperLevel,1); % solve function using GA
% display the fitness value
fprintf('simple bi-level case: fit = %d\n',UpperLevel(x1));
fprintf('Upper Level Sol:x1 = %d \n', x1);
fprintf('Lower Level Sol:x2 = %d \n', LowerLevel(x1));

% you can noticed the results is clost to our analitical results. 