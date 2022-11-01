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
