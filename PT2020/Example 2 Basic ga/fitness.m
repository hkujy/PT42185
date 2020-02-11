function [value] = fitness(x)
    % the fitness function is to minimize sum x^2
    value = 0;
    for i=1, size(x,2);
        value = value + x(i)^2;
    end 