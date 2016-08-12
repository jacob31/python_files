# file name: mean.py
# author: Ben Silbernagel
# created: 5/27/2016
# purpose: to calculate the mean from a data set plus alpha parameters
#         I think this was from a datacamp project or dataquest
 


# Calculate mean from data set.

# data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]
# data2 = [79.519999999999996, 24.300000000000001, 19.870000000000001, 91.450000000000003, 25.800000000000001, 90.280000000000001, 74.859999999999999, 5.5199999999999996, 72.659999999999997, 93.950000000000003, 63.539999999999999, 99.549999999999997, 22.059999999999999, 52.030000000000001, 72.790000000000006, 59.340000000000003, 49.0, 15.859999999999999, 79.510000000000005, 22.82, 40.909999999999997]
#
# def mean(data):
#     return sum(data) / len(data)

#print mean(data1)
#print mean(data2)

#Hypothesis Testing
import math

# population parameters
mew = 7.47 #population mean
sigma = 2.41 #standard deviation

#sample parameters
n = 50 # sample size
xbar = 8.3 # sample mean
standard_error =  sigma / (math.sqrt(n))# sample standard deviation
sample_z_score = (xbar - mew) / standard_error

# alpha parameters for critical regions
two_tailed_test = False # c
alpha_1 = .05
alpha_2 = .01
alpha_3 = .001

print sample_z_score
