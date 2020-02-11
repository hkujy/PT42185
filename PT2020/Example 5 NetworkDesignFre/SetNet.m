% set nework
% link 1: 1->2
% link 2: 2->1
% link 3: 2->1
% link 4: 2->1
% link 5: 2->1
% link 7: 2->1
% link 8: 2->1
s = [1 2 1 3 2 3 3 4];
t = [2 1 3 1 3 2 4 3];
weights = [5 5 10 10 25 25 16 16];
names = {'1','2','3','4'};
G = digraph(s,t,weights,names);

% route information 
% route 1: 1 -> 2: Time = 5
% route 2: 1 -> 2 -> 3: Time = 30
% route 3: 1 - >3 : Time = 10
% route 4: 1 - >3 -> 4 : Time = 26


