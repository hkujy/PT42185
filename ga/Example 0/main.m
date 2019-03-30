clear; clc;

%% Example 1: integer -> binary

% integer -> binary
x = 10;
binary_x = dec2bin(x);  % return binary Character 
% binary -> integer
y = bin2dec(binary_x);


%% Example 2:  Binary -> continous value

% binary_x to continous value
x = [1,0,1,0,0,1,1,0];
y=decode(x,0,100,2);