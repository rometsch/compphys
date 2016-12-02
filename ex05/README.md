# Interpolation

## Lagrange-Interpolation of Equation of States

Run `interpolation.py` to produce data and many many plots.

## Plot of chi square errors

Load `plot_error.plt` with gnuplot to produce the plot of errors for three intervals.
Clearly the larger interval with the feature in just a small part of the interval shows overfitting with the Lagrange-Polynomials.
This also gets clear considering the diverging errors in the error plot.

## Animations of the convergence

Run `make_videos.sh` to generate animations out of the plots produced earlier.
You need `ffmpeg` to be installed on your system.
Also a folder `video` will be created.

## Note

The plot of errors and the videos showing the convergence or divergence are already stored in the repository.
