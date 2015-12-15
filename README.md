Monte Carlo Pi approximation
=============
Python code that approximates the value of pi based on the randomly generated points inside a unit square and a unit circle. Pi is approximated using Probability theory, therefore increasing the size of the sample (randomly generated points) and number of passes would give a better approximation of pi.


### Usage
```python
from mc_pi import calc_pi

#Approximate pi with 1000 random data points and average value of pi over 10 passes
print calc_pi(sample=1000,passes=10)
```
Ploting of sample data works only with single passes, because multiple passes will cause large output of matplot lib charts.
```python
from mc_pi import calc_pi

sample_size = 1000
#Plot single pass data:
    print "Monte Carlo pi, single pass, sample size = {}, pi = {}".format(
        sample_size,calc_pi(sample = sample_size, plot=True))
```
Output of plot:
-------------
![Sample plot](http://i.imgur.com/hJjd2Xu.png)

To check peformance of approximation module on your system you can use timeit somewhat similar to this:
```python
import timeit
from mc_pi import calc_pi

if __name__ == '__main__':
    
    #Test performance of calc_pi using timeit
    print timeit.timeit("print calc_pi(sample=8000,passes=10)",
        setup="from __main__ import calc_pi", number=1
    )
```
