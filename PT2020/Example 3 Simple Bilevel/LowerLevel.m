function [LowerLevelSol] = LowerLevel(UpperLevelSol)
    x1 = UpperLevelSol;
    
    fun = @(x2)2*x1^2-x1*x2+x2^2;
    
    x2_initial_guess = 0;
    x2 = fminsearch(fun,x2_initial_guess);
    
    LowerLevelSol = x2;