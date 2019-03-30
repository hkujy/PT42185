function [fit] = UpperLevel(UpperLevelSol)
% given upper level solution 
% solve lower level problem first 

LowerLeveSol = LowerLevel(UpperLevelSol);

x1 = UpperLevelSol;
x2 = LowerLeveSol;

fit =  x1^2-x1*x2+2*x2^2+x1; % only the upper level objective function
