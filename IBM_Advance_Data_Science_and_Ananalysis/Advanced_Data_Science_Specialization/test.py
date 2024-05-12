from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "test")
rdd = sc.parallesize(range(100))
sum = rdd.sum()
n =rdd.count()
mean = sum/n
print (mean) 
rdd.sortBy(lambda x : x).zipWithIndex().map(lambda (value,key) : (key, value)).collect()
n = sortedAndIndexed.count()
if (n % 2 == 1) :
    print ('odd case')
else:
    print ('even case')
#dvd