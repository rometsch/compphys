clear
reset

file1 = "d1.0e-03.txt"
title1 = "dt = 1e-3"
file2 = "d5.0e-04.txt"
title2 = "dt = 5e-4"
file3 = "d1.0e-06.txt"
title3 = "dt = 1e-6"

set title "Lorenz Attractor, sigma = 10, R= 28, beta = 8/3\nDistance of trajectory for inital conditions (5,5,5) and (5,5,5+1e-5)"

set box

set grid

set key right bottom

set logscale y

set format y "%.1e"

set xlabel "t"
set ylabel "d"

plot file1 u 1:2 title title1 pt 1, file2 u 1:2 title title2 pt 2#, file3 u 1:2 title title3 with dots

pause -1
