function z = Objective(x)

t(1) = 2 + x(1);
t(2) = 1 + 2*x(2);

u = min(t);

z = x(1)*(t(1)-u) + x(2)*(t(2)-u);

end