
% reference: practical genetic algorithms

function [y] = decode(binary_matrix,LowerBound,UpperBound,nbits)
% binary_matrix presents the binary ga
% return the continous value 


lo = LowerBound;   % lower bound value
hi = UpperBound;   % higher bound value
[M,N]=size(binary_matrix);
npar=N/nbits; % number of variables
quant=(0.5.^(1:nbits)'); % quantization levels
quant=quant/sum(quant); % quantization levels
%normalized
ct=reshape(binary_matrix',nbits,npar*M)';% each column contains
% one variable
par=((ct*quant)*(hi-lo)+lo); % DA conversion and
% unnormalize varaibles
y=reshape(par,npar,M)';% reassemble population



