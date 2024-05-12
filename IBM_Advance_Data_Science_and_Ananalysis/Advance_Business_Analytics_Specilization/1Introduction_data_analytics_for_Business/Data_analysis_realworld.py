'''''
Data and Analysis in the Real World : 
#A conceptional business model is a diagram that illustrates how an industry 
or business functions. It shows important element in the business and 
maps out how those elements relate to each other. 

Information-Action Value Chain :
Steps before analysis:
#1 Real-world events and chracteristics 
#2 System data capture 
#3 Accessible Location / Storage
#4 Data Extraction for Analysis 

Type of Analytics:
#Descriptive : As its name suggests, helps us describe what things look
like now or what happend in the past. The idea of course is to use that 
information to better undertand the business enviroment and how it works.
And make better decision.Simple statistical measures like means, medians
and standart deviations. More sophisticated statistics like distributions,
confidence intervals and test of hypotheses or advanced association or
clustering algorithms.
#Predictive : It help us take what we know about what happened in the past
and use that information to help us predict what will happen in the future.
This almost always involves the application of advanced statistical methods 
or other numeric techniques such as linear or logistic regression. Tree based
algorithms, neural networks and simulation techniques such as Monte Carlo simulation.
#Prescriptive : This type of analysis  helps explicitly link analysis to decison 
making by providing recommendations on what we should do or what choice we 
should make to achieve a certain outcome. It usually involves the integration of 
numerical optimization techniques with business rules and even financial model. 

#5 Summarize and Interpret Results
#6 Develop Strategy and Plan
#7 Deliver The Pitch 
#8 Take Action 








More Details 

#2 System data capture
- Core enterprise systems : Billing and Invoicing, Enterprise resource, Planning these are usually large scale system that tie in directly 
to the financial operations of company.They include things like billing and invoicing
systems that help manage purchasing transaction and the collection of payments.they also
include enterprise reprise planning or ERP systems, which are really broad systems to help 
manage business processes on the back end of the business.Supply chain management system 
focus specifically on the flow and storage of goods and services through a system.
- CRM systems are used to track and manage customes interactions across all touch points
and throughout the customer life cycle with company. 
- Customer and People stytems: CRM , customer care, lead management- sales force outomation,
campaign management, human resource, electronic health medical records.
- Product and presence systems : Product management, content management, web management analytics
- Technical operation systems: Process monitoring, alarming and fault monitoring, ticketing and workflow management,
telematics and machine, data processing.
- External source systems : Credit agencies, demographics and segmentation providers, partners and suppliers. 


#Data Storege and Databases 
- An Online Analytical Processing OLAP terms refer to storege systems that are optimized for business
operations and transactions versus those that are optimized for analytics.
-Source systems often deal with very high volumes of data, they may not store data for very long in order to optimize
the overal performance of that system. This means that if we want the data or some subset of the data to be available for
a longer period of time we need to grab it anf put it in a longer term storage location. 
-However a more common solution is to gather into a separate storage location.
This may be central data repository, a virtual repository or combination of these two things or a semi centralized repository.
- File Systems can handle unstructured data.Limited in readliness for use and interconnectivity. 
- Hadoop Distributed File Sytem (HDFS)
-Data types are XML, Text, Excel, log files.
-Database Management System is a softaware application use for creating, maintining and accessing databases.Most common is the Relational Database.
-Common Altenative Databases : Graph databases, document stores, columnar databases and key value stores.

#Big Data and the Cloud Computing

- Generally speaking, big data refers to the idea that certain emergent data sources like machine data and web-based data 
generate a huge amount of information that can't be easily processed by traditional tools. 
- Consequently, big data also refers to the broad class of tools that are also used
to capture, store, process, and analyze these high-volume data sources.
- Cloud computing, on the other hand, really just speaks to where these operations happen. 
- Traditionally, most computing operations were done with
machines and software owned and operated by the organizations that needed them.
- With Cloud computing, organizations can effectively rent hardware capacity, software, and services from a third party,
that runs everything in the third party's data centers. Big data and cloud computing are certainly complementary technologies.
- There can be substantial advantages to executing big data operations in the cloud. 
- However, its important to recognise that we can have big data without the cloud, and we can have the cloud, even if we don't have big data.
- In the big data landscape as Hadoop on premise, Hadoop in the cloud, No SQL databases, new SQL databases, graph databases, and PP databases and Cloud EBW.
- Big data analytics tools seek to perform the same types of descriptive, predictive and prescriptive analytics that we perform in any enviroment but enable 
the ability to do it on very large datasets and potentially in real time.
- Infrastructure broadly refers to the hardware networking, management and security aroud a data enviroment.
- Hadoop Framework HDFS and a processing algorithm called MapReduce are examples of how big data technologies enable efficient infrastructure.
- Software as a service SaaS, platform as a service PaaS and Infrastructure as a service IaaS.
- Additionally, using Cloud services can remove a lot of distraction and overhead from the customer organization since much of the administration, back up, redundancy and disaster will cover out responsibilities or handled by the service provider. This means that organizations can run leaner and be more focused on their core business functions

#Vitualization, Federation and In Memory Computing

- When we talk about storing data and making it available for data analytics we usually describe our process where data is physically moved from various source systems
into a common location like a database. This usually happens using something called an extract, trasnform and load or ETL process.
- Data virtualization is that we keep source data where it is for each source but we make it look like all the data is in  one place and we allow users to access that data using one common interface.
One advantage of data virtualization is that we can avoid having to store data in multiple places, namely in the source system and in some target database.
- With data federation, not only do we make it look like data is in one place, but we actually fit that data into a common integrated data model.

# The Relational Database

- DBMS which is asoftware application used for creating, maintaining and accessing databases.
- The applications that run relational databases are called relational database management systems or RDBMS.
- In relational databases, we store information in tables and then define specific relationship among those tables.
- Why are relational databases so popular?
- Allows data to be grouped logically around dicrete ideas
- Minimizes the amount of duplicate data stored in a database
- Minimizes the number of places where changes to data need to be made
- Improves performance in highly transactional systems where lots of updates and additions are made
- Is incredibly flexible in terms of how data can be queried and extracted.
- Relational databases uniqueness and primary keys: Natural, surrogate, composite
Foreign keys and table linkages normalization and 3NF denormalization.

# Data Tools Landscape
# The Tools of the Data Analyst

- We will start looking at three broad methodologies a data analyst might employ to access and analyze data.
- First one is the intermediate file approach. In this approach we extract data from a database or other location where data 
is stored and we export the data we need in to a standalone file like a text file or Excel file.The often involves 
writing SQL code against the database to extract just the data we need. We then import the data into an analytical tool like Excel a business intelligence
tool or a statistical software package or programming enviroment.Once the data is in the analytical enviromenmet i can execute whatever type of analysis is desired.
Note that this approach assumes that all the data i need is already integrated in one database environment.
So why might I use this approach? For starters, you might not be able to connect your analytical tools directly to your database due to security or stability concerns. 
Or you may not have time to set up all the permissions and network connections required to make a direct connection. It might be the case that you need to extract the 
data at one point in time and analyze it later or analyze it offline. You might also want to drive the same data set into multiple analytical tools. In these cases, 
it's more convenient to store the data in an intermediate file and import it for analysis. 
- Second method might be called the direct connection approach.Finally, by breaking access into two steps I have a little mores control and visibility into each steps, 
which might be useful for data validation and quality control. A second method might be called the direct connection approach. Wth this approach we connect our analytics
tool directly to a database or other data source using what's called an open database connectivity, or ODBC connection, or some other application program interface or API connection. 
Broadly, APIs are standard mechanisms for exchanging information between programs, and ODBC is one special case of an API used to connect to databases. 
- The last method we'll cover is what we'll call the downstream integration approach. It's quite often the case in data analytics that the information we need is located in a bunch of 
different locations and formats. While it would be nice to have everything on one warehouse, it doesn't always makes sense to spend the time and energy to put everything there prior to analysis. 
Especially if we're not entirely sure those sources will turn out to be important



# Introduction SQL 
- SQL was developed in the early 1970s to help users manipulate and extract data from those databases. It's a language that's based on relational algebra, 
which is a set of mathematical operations that speak to how things are related, like intersections, unions and differences.


'''''