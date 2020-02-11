A=[];
b=[];
Aeq=[1,1];
beq=[5];  %total flow
lb=[0;0];
ub=[inf;inf];
x0=[0;5]; %initial flow

x = fmincon(@(x)Objective(x), x0, A, b, Aeq, beq, lb, ub);

% print x 
x



