import timeit
from mc_pi import calc_pi

if __name__ == '__main__':
    
    #Test performance of calc_pi using timeit
    print timeit.timeit("print calc_pi(sample=8000,passes=10)",
        setup="from __main__ import calc_pi", number=1
    )
    
    sample_size = 10000
    passes = 10
    
    #Single Pi value approximation
    print "Monte Carlo pi value of sample size {} and single pass: {}".format(
        sample_size,calc_pi(sample=sample_size))
    
    #Multiple passes pi value average
    print "Monte Carlo pi value of sample size {} and {} passes: {}".format(
        sample_size,passes,calc_pi(sample=sample_size,passes=passes))

    #Plot single pass data:
    print "Monte Carlo pi, single pass, sample size = {}, pi = {}".format(
        sample_size,calc_pi(sample = sample_size, plot=True))