clear
reset

file1 = "RK4.txt"
title1 = "RK4"
file2 = "Adams_Multon_WoCorr.txt"
title2 = "Adams Multon without Corr"
file3 = "Adams_Multon_Corr.txt"
title3 = "Adams Multon with Corr"

set box

set grid

set key right top

set logscale xy

set format x "%.0e"
set format y "%.0e"

set xlabel "N"
set ylabel "error"

plot file1 u 1:2 title title1 pt 1, file2 u 1:2 title title2 pt 2, \
      file3 u 1:2 title title3 pt 4

pause -1
