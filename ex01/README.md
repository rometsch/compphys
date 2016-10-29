# rootfinding

## run the program
Use python3 to run.
`python3 rootfinding.py`

## verbosity of output
In `main()` you can specify the verbosity of the output.
Set verbosity to
  * 0 for minimal output
  * 1 for file output to be used in gnuplot
  * 2 for output of each iteration

## plotting
Execute `gnuplot plotscripts/plot_error.gnu` to get plots of the errors.
Expected functions of the errors are fitted to the values.

For this, data must be present in the `results` folder in seperate files for each method. Use `verbosity=1` option.

In this repository, these files are already present.
