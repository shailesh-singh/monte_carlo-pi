monte_carlo-pi
=============
Python code that approximates the value of pi based on the randomly generated points inside a unit square and a unit circle. Pi is approximated using Probability theory, therefore increasing the size of the sample (randomly generated points) and number of passes would give a better approximation of pi.


### Usage
```python
#Approximate pi with 1000 random data points and average value of pi over 10 passes
print calc_pi(sample=1000,passes=10)
```
