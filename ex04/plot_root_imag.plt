outputfile = datafile."_imag.png"

set terminal pngcairo size 1000,800 font "Helvetica,12" linewidth 1 rounded
set output outputfile

set pm3d depthorder
set view map

set title "Imaginary part of the root of f(z) = z^3 -1 calculated with Newtons Method"

set size ratio -1

set xlabel "Re(z)"
set ylabel "Im(z)"
set zlabel "Im(k)"

splot datafile u 1:2:4 with pm3d
