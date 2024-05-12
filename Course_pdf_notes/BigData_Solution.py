'''''

# Tools That Support BigData Solutions
- SQL Databases has advantage for BigData Solution 
- The Hadoop Distributed File System (HDFS) is a distributed file system designed to store large volumes of data
reliably and efficiently across multiple machines
- A remote relational database behaves basically like a remote file system. 
- Data stored in RDDs is only read from the underlying storage systems when needed. 
- ApacheSpark a framework for processing Big Data : fast big data processing, built-in modules for streaming, SQL
machine learning, graph processing. Framework is reusable set of libraries. ApacheSpark programs when implemented in 
R are only slow when a lot of local executions withing R libraries takes place. 
- Programming language options on ApacheSpark are Scala which future language, Python, R ,Java. 



# Data Storage Solution 
- In case you have a low amount of data and a very stable schema, you can go for SQL. As the amount of data increases, 
all you have to cope with continuously changing schemas, you should go for NoSQL. 
Finally, on very high amounts of data or very unstable schemas, even including audio, images, and video data, 
the primary choice is ObjectStorage.


# Parallel data processing strategies of Apache Spark
- When we talk about ApacheSpark we talk about a Java Virtual Machine.JVM is compatible programming language.
- If we want to use large compute clusters but still don't want to take care of parallelizing our programs, ApacheSpark kicks in.
- In computing, cluster refers to group of interconnecting computer or server that work together to perform a specific task or provide a service.
- Let's consider a file, too big to fit on a single disk.What we have to do then is divide it in equal size chunks and 
distribute them over the physical disks.This is where HDFS comes into play.HDFS creates a virtual view on top of those chunks so 
that it can be treated as a single large file spanning the whole cluster.
- RDD stands for Resilient Distributed Dataset. It's a fundamental data structure in Apache Spark, 
a popular open-source distributed computing framework. 
- RDDs are lazy. What does this mean? Data stored in RDDs is only read from the underlying storage systems when needed.
This concept is called lazy evaluation and due to the inventors of functional programming languages. 
This means that functions are only executed if the output of their computations is needed for further downstream data processing.
Other programming becomes easy when using ApacheSpark because when using the RDD API you simply can't write non parallel programs.
It doesn't matter how much data you process, the program always stays the same. RDD provides the central API for achieving this. 
And you don't have to worry about data and task distribution. ApacheSpark will handle this for you.


# Difference between database and dataset 
- Database : a database is a structured collection of data that is organized and stored in a way that enables efficient retrival, updating and management.
Databases are typically designed to store large volumes of structured data in tables, with each table consisting of rows and columuns. 
They use a database management system (DBMS) to manage and manipulate the data.
Databases can be relational (SQL databases like  MySQL, PostgreSQL) or non-relational
(NoSQL databses )
Databases are commonly used in applications that require persitent storage of data such as transactional systems and web services.
- Dataset : A dataset is a collection of related data records or observations that are grouped 
group together for analysis, processing and presentation.
Dataset can be structured unstructered and semi-structured depending on the nature of the data they contain. 
Datsets are often used in data analysis, machine learning, statistical analysis and other data driven tasks.



# Functional programming basics
- ApacheSpark parallelises computations using the lambda calculus.
- All functional spark programs are inherently paralel. 
- Scala: This is the primary and native language for GraphX. 
Spark itself is written in Scala, and GraphX leverages Scala's functional programming features for efficient graph processing.


# Introduction of Cloudant 
- Cloudant is a NoSQL database as a service, and actually has some unique features which can't be found in other NoSQL databases.


# Resilent Distributed Dataset and Dataframes - ApackSparkSQL
-  Apache Spark SQL provides an LC 2003 compliant SQL interface to your data. The RDD is still a first class citizen, so what 
ApacheSparkSQL basically does is wrapping the RDD with a DataFrame object actually abstracting the API to a relational one. 
You always can access the underlying RDD, but now in addition to that, you have a relational API on top of your data.
- So the Java Virtual Machine is a piece of art by itself. It is a general purpose byte code execution engine, 
which is suited for a huge variety of applications from mobile devices to large clusters of server machines.
- Catalyst and Tungsten are able to optimize the execution, so are more likely to execute more quickly than 
if you would had implemented something equivalent using the RDD API.
The API is simpler and doesn't require specific functional programming skills.
These options highlight the advantages of using Apache Spark SQL over RDDs.



 '''''

'''''
# Scaling Math for Statistics on Apache Spark

1st Statistical moment:
'Avarages' -Measures of Central Tendecy. Mean and median. 


'''''