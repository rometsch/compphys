clear
reset

folder = "f2/"

file1 = "integrate_trapezoidal.txt"
title1 = "trapezoidal"

file2 = "integrate_gauss_legendre_2.txt"
title2 = "gauss legendre 2"

file3 = "integrate_gauss_legendre_4.txt"
title3 = "gauss legendre 4"

file4 = "integrate_gauss_legendre_8.txt"
title4 = "gauss legendre 8"

file4 = "integrate_gauss_legendre_8.txt"
title4 = "gauss legendre 8"

file5 = "integrate_2nd_newton_cotes.txt"
title5 = "Newton-Cotes 2nd order"

file6 = "integrate_simpson.txt"
title6 = "Simpson 3/8"

set title "integration of function f2"

set grid

set key right bottom

set format x "%.1e"
set format y "%.1e"

set logscale xy

set xlabel "h"
set ylabel "error"

plot folder.file1 u 1:2 title title1, folder.file2 u 1:2 title title2, \
    folder.file3 u 1:2 title title3, folder.file4 u 1:2 title title4, \
    folder.file5 u 1:2 title title5, folder.file6 u 1:2 title title6

pause -1
