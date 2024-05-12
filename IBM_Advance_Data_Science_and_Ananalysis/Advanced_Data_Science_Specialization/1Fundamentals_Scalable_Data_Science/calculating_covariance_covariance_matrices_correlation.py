from pyspark import SparkContext
# Initialize SparkContext
sc = SparkContext("local", "test")

rddX = sc.parallelize(range(100))
rddY = sc.parallelize(range(100))

meanX = rddX.sum()/rddX.count()
meanY = rddY.sum()/rddY.count()

rddXY = rddX.zip(rddY)
#covXY = rddXY.map(lambda (x,y) : (x-meanX)*(y-meanY)).sum()/rddXY.count()
print(covXY)

from math import sqrt
n = rddXY.count()
sdX = sqrt(rddX.map(lambda x : pow(x-meanX,2)).sum()/n)
sdY = sqrt(rddY.map(lambda x : pow(x-meanY,2)).sum()/n)

corrXY = covXY / (sdX * sdY)
print(corrXY)
