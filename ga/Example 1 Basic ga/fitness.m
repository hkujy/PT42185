function [value] = fitness(x)
    value = 0;
    for i=1, size(x,2);
        value = value + x(i)^2;
    end 