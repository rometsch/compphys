clear

file = "errors.txt"

set key top left
set xtics (3,4,5,6,7,8,9,10,20,30,40)

set logscale xy

set grid

set xlabel "number of datapoints"
set ylabel "chi square error"

set xrange [2.9:41]

plot file u 1:2 title "I = [4.5, 5.5]", file u 1:3 title "I = [0, 10]", file u 1:4 title "I = [0, 30]"

pause -1
