module helloworldfpga(

input  wire X,
input  wire Y,
input  wire Z,
input  wire W,


output wire A,
output wire B

);


//Display Decoder
always @(*)
begin


A= X||Z;
B= Y||Z;



end
endmodule


#!/bin/bash

ql_symbiflow -compile -src /sdcard/Download/iith/iith/vaman/Assignment-10/codes -d ql-eos-s3 -P PU64 -v Assignment10.v -t helloworldfpga -p Mypins.pcf -dump binary
