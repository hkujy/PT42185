function [fit] = Fitness(NetworkSol)

% step 1, revise network structure based on the input
s = [1 2 1 3 1 4 2 3 2 4 3 4];
t = [2 1 3 1 4 1 3 2 4 2 4 3];
weights = [5 5 2 2 4 4 6 6 4 4 1 1];
% set the network weight such that each link has a very large value of
% travel time

NewWeights = [1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000];
names = {'A','B','C','D'};

% if the link is selected to build, then the link cost is set to be default

for i=1:size(NetworkSol,2)
    LinkId = NetworkSol(i);
    NewWeights(LinkId) = weights(LinkId);
end

NewG = digraph(s,t,NewWeights,names);

fit  = 0;
[P,d] = shortestpath(NewG,'A','B');
fit = fit +d;
[P,d] = shortestpath(NewG,'A','C');
fit = fit +d;
[P,d] = shortestpath(NewG,'A','D');
fit = fit +d;

