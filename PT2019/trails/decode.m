%function f=decode(chrom,lo,hi,bits)

chrom = [0,0,0,1,1,0,1,1];
lo = 1;
hi = 2;
bits=2;
[M,N]=size(chrom);
npar=N/bits; % number of variables
quant=(0.5.^[1:bits]'); % quantization levels
quant=quant/sum(quant); % quantization levels
%normalized
ct=reshape(chrom',bits,npar*M)';% each column contains
% one variable
par=((ct*quant)*(hi-lo)+lo); % DA conversion and
% unnormalize varaibles
f=reshape(par,npar,M)'; % reassemble population