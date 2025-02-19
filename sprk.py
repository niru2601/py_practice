import pyspark

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('example').getOrCreate()

spark.read.option('header','true').csv('C:\\Users\\niranjan.patil\\Downloads\\test.csv').show()

