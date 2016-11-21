outputfile = datafile."_Niter.png"

set terminal pngcairo size 1000,800 font "Helvetica,12" linewidth 1 rounded
set output outputfile

set pm3d depthorder
set view map

set title "Log10 of number of iterations needed to converge with Newtons Method"

set size ratio -1

set xlabel "Re(z)"
set ylabel "Im(z)"
set zlabel "Im(k)"

splot datafile u 1:2:7 with pm3d
