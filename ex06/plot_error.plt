clear

file1 = "errors_t0.000.txt"
file2 = "errors_t2.094.txt"

set key top right

set logscale xy
set ytics format "%.1e"

set grid
set xrange [9.9e-4:1.26e-1]

set xlabel "h"
set ylabel "estimated error"

plot file1 u 3:2 title "t=0",file2 u 3:2 title "t=pi/delta omega"

pause -1

outname = "error_plot.pdf"
set terminal pdfcairo size 5,3 font "Helvetica,10" linewidth 1 rounded fontscale 0.6
set output outname

replot
