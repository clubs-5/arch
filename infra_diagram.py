from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import CloudFront
from diagrams.aws.network import CloudMap

with Diagram('Simple Diagram'):
    EC2('crawler') >> CloudFront('www')
    CloudMap('www')
