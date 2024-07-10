// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/01/Mux16.tst

load DMux16.hdl,
output-file DMux16.out,
compare-to DMux16.cmp,
output-list in%B1.16.1 sel%D2.1.2 a%B1.16.1 b%B1.16.1;

set in %B0000000000000000,
set sel 0,
eval,
output;

set sel 1,
eval,
output;

set in %B1111111111111111,
set sel 0,
eval,
output;

set sel 1,
eval,
output;

set in %B1010101010101010,
set sel 0,
eval,
output;

set sel 1,
eval,
output;

set in %B0101010101010101,
set sel 0,
eval,
output;

set sel 1,
eval,
output;