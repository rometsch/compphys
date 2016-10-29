datafile1 = "result_newton.txt"
datafile2 = "result_linear_interplation.txt"
datafile3 = "result_bisection.txt"

r = 7.53701168414018e-01; # root of the function

outname='errors.pdf';

curve1='Newton'
curve2='linear interpolation'
curve3='bisection'

set xlabel "iteration"
set ylabel "error"

# Zehnerpotenzen in y tics
set format y "10^{%L}"

set decimalsign '.'

#set xrange [1:9]
set yrange [1e-16:1e1]
set grid
set key box opaque height 2 right top


set log y
#set log x

# Beschriftung für die Kurven
set style line 1 lt rgb "#A00000" lw 1 pt 1
set style line 2 lt rgb "#00A000" lw 1 pt 2
set style line 3 lt rgb "#5060D0" lw 1 pt 3
set style line 4 lt rgb "#F25900" lw 1 pt 5
set style line 5 lt rgb "#A25900" lw 1 pt 7

# fit errors to compare constants
fit_bisection(x) = exp(fit_bisection_exponent(x));
fit_bisection_exponent(x) = c1b+c2b*x;
m = (1+sqrt(5))/2;
k = 1.8;
eps0 = 1;
c1b = log(k)/(1-m);
c2b = log(eps0)-log(k)/(1-m);
fit fit_bisection_exponent(x) datafile3 using 1:(log(abs($3-r))) via c1b,c2b;

fit_interpol(x) = exp(fit_interpol_exponent(x));
fit_interpol_exponent(x) = c1i+c2i*x;
m = (1+sqrt(5))/2;
k = 1.8;
eps0 = 1;
c1i = log(k)/(1-m);
c2i = log(eps0)-log(k)/(1-m);
fit fit_interpol_exponent(x) datafile2 using 1:(log(abs($3-r))) via c1i,c2i;

fit_newton(x) = exp(fit_newton_exponent(x));
fit_newton_exponent(x) = c1n/(1-m)+(c2n-c1n/(1-m))*m**x;
m = 2;
k = 3.6;
eps0 = 0.37;
c1n = log(k);
c2n = -0.9948;
fit [x=5:] fit_newton_exponent(x) datafile1 using 1:(log(abs($3-r))) via c1n,m;


# print fit results
print("Bisection method:");
print(sprintf("exponent = %f",c2b));

set terminal pdfcairo size 5,3 font "Helvetica,10" linewidth 1 rounded fontscale 0.6
set output outname

# Plot von Daten
plot datafile1 using 1:(abs($3-r)) title curve1 ls 1,\
  fit_newton(x),\
	datafile2 using 1:(abs($3-r)) title curve2 ls 2,\
  fit_interpol(x),\
	datafile3 using 1:(abs($3-r)) title curve3 ls 3,\
  fit_bisection(x)

unset output
reset
