from pyspark import SparkContext
# Initialize SparkContext
sc = SparkContext("local", "test")
rdd = sc.parallelize(range(100))
sum = rdd.sum()
n = rdd.count()
mean = sum/n
print(mean)

#Calculating standart deviation: Standart deviation is commonly used in various field such as finance, statistics and science to undertand the uncertainity assosiated with a set of data.
#The expression i provided seems to be a calculation of the variance of a 
#Using the RDD API in Apache Spark. 
from math import sqrt 
sd = sqrt(rdd.map(lambda x : pow(x-mean,2)).sum()/n )

#Calculating Skewness 
#Skewness tells us about asymmetry of data around mean value 
n = float(n)
skewness = (1/n)*rdd.map(lambda x : pow(x-mean,3)/pow(sd,3)).sum()

#Kurtosis measures the 'tailedness' of distribution, with higher values
#indicating heavier tails and lower values indicating lighter tails compared to the normal distribution.
#Reports on the shape of the graph and the relative number of outliers.
''''' 
If the kurtosis is:

Less than zero (negative): The distribution is platykurtic, meaning it has thinner tails and is less peaked than a normal distribution.
Equal to zero: The distribution has the same kurtosis as a normal distribution (mesokurtic).
Greater than zero (positive): The distribution is leptokurtic, meaning it has heavier tails and is more peaked than a normal distribution. '''''
kurtosis = rdd.map(lambda x : pow(x-mean,4)/pow(sd,4)).sum()/n