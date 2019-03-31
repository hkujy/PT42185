clear; clc;

%% Example 1: decode GA representation to variables

% case 1: if the decision variables are integer
x = 10; binary_x = dec2bin(x);  
y = bin2dec(binary_x);


%% Case 2: if the decsion varible is continous variable given upper and lower bound 

% binary_x to continous value
x = [1,0,1,0,0,1,1,0];
y=decode(x,0,100,2);