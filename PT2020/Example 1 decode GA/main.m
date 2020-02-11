clear; clc;

%% Example 1: decode GA representation to variables

% case 1: if the decision variables are integer
x = 10;   % Input variable x
binary_x = dec2bin(x)  % convert x to binary 
y = bin2dec(binary_x)  % convert back binary x to integer 


%% Case 2: if the decsion varible is continous variable given upper and lower bound 

% binary_x to continous value
% given integer variable
% x represent 4 numbers, each number is represented by 2 binary bits
x = [1,0,1,0,0,1,1,0]    % given integer variable
y=decode(x,0,100,2)      % convert x to decimal value
