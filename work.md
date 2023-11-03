# Amazon RDS 
amazon rds allows us to create relational databases. 
Relational databases are used to store data for a wide variety of applications. Relational databases use normalised database table designs, which means that data is stored across multiple tables with defined relationships between the tables.

# nosql
NoSQL databases run on a group of servers called a cluster, each with its own fixed amount of memory and compute capacity. If better performance is needed, additional servers can be added to the existing cluster group.
 
DynamoDB is a NoSQL database: 
Fully Managed Service: AWS handles all underlying compute and storage for data storage.
Scalability: DynamoDB automatically adds more compute and storage capacity as your data grows.
Redundancy: DynamoDB copies your data across multiple AWS Regions to avoid data loss.
Recoverability: DynamoDB can restore your data from automatic backup operations.
Low Latency: Data can be read from a DynamoDB table in a few milliseconds.
Security: You can use DynamoDB with AWS Identity and Access Management (IAM) to control access to DynamoDB tables.
Flexibility: DynamoDB can store several types of data, and each record can have varying numbers and types of data. JSON is one popular way to store data in DynamoDB.

The DynamoDB global tables feature provides high availability and scalability across Regions. A global table is a collection of one or more DynamoDB tables, which must all be owned by a single AWS account. The tables in the collection are also known as replica tables. Each replica stores the same set of data items

