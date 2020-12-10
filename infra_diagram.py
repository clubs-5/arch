from diagrams import Diagram,Cluster,Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import CloudFront
from diagrams.aws.network import CloudMap
from diagrams.onprem import analytics,compute,database
from diagrams.elastic import elasticsearch
from diagrams.programming import language,framework
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Users,Client

with Diagram('Simple Diagram'):
    internet = CloudMap('internet')
    crawler = EC2('Python Crawler')
    rdb = database.Mysql('RDB')
    #nosql = database.MongoDB('NoSQL')
    es = elasticsearch.Elasticsearch
    predictior = language.Python('Machine Learning/Analytics')
    backend = framework.Flask('Backend')
    #users = Users('users')
    client = Client('client')
    
    with Cluster('HDFS Cluster'):
        hdfs_master = compute.Server('NameNode')
        cluster = [hdfs_master, 
                   compute.Server('DataNode1'),
                   compute.Server('DataNode2'),
                   compute.Server('DataNode3')]

        
        
        
    internet >> crawler >> Edge(color='orange') >> cluster >> rdb >> predictior >> backend >> client
