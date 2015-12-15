from __future__ import division 

import timeit #used for benchmarking peformance
import random 
from matplotlib import pyplot as plt

def calc_pi(sample=0,passes=1,plot=False):
    """Calculates Pi using Monte Carlo Method
    
    Returns: average of pi values of all passes

    Parameters:
    -----------
    sample: sample size in integer value
    passes: number of passes in integer value
    plot: boolean value for ploting data. set to True for plot of single pass"""
    if passes > 1 and plot == True:
        raise ValueError("Plots work with only one pass\n\
        Either set passes to 1 or remove pass from parameter"
        ) 
           
    vals=[]
    for a in range(0,passes):
        x = [random.uniform(-1,1) for _ in range(0,sample)]
        y = [random.uniform(-1,1) for _ in range(0,sample)]
        
        unit_circle = filter( lambda i: i[0]*i[0] +i[1]*i[1] <= 1, zip(x,y))
        
        vals.append(4*len(unit_circle)/len(x))
        

    
    if plot:
        x_2 = [i for i,_ in unit_circle]
        y_2 = [j for _,j in unit_circle]
        fig = plt.figure()
        plt.scatter(x,y,color='b')
        plt.scatter(x_2,y_2,color='r')
        plt.show()
    
    return sum(vals)/len(vals) # returns average of number of passes




if __name__ == '__main__':
    
    #Test performance of calc_pi using timeit
    print timeit.timeit("print calc_pi(sample=8000,passes=10)",
        setup="from __main__ import calc_pi", number=1
    )
    
    sample_size = 10000
    passes = 10
    
    #Single Pi value calculation
    print "Monte Carlo pi value of sample size {} and single pass: {}".format(
        sample_size,calc_pi(sample=sample_size))
    
    #Multiple passes pi value average
    print "Monte Carlo pi value of sample size {} and {} passes: {}".format(
        sample_size,passes,calc_pi(sample=sample_size,passes=passes))

    #Plot single pass data:
    print "Monte Carlo pi, single pass, sample size = {}, pi = {}".format(
        sample_size,calc_pi(sample = sample_size, plot=True))