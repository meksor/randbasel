# randbasel
A short python script to copmute an aproximation of PI via the probability of [two random numbers being coprime](http://www.cut-the-knot.org/m/Probability/TwoCoprime.shtml) and the [basel problem](https://plus.maths.org/content/basel-problem).   

Currently 256^3 Iterations and random numbers generated between 0 and 256^2.  


It uses the standard python libaries:
 - random
 - fractions
 - math
 - sys (sys.maxsize to use the maximum integer size of your system!)

`python randbasel.py`
