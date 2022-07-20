from flytekit import Resources, task, workflow
from flytekitplugins.spark import Spark
import flytekit

@task(
    task_config=Spark(
        # this configuration is applied to the spark cluster
        spark_conf={
            "spark.driver.memory": "1000M",
            "spark.executor.memory": "1000M",
            "spark.executor.cores": "1",
            "spark.executor.instances": "2",
            "spark.driver.cores": "1",
            "spark.jars.packages": "org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.11.375,org.apache.hudi:hudi-spark3.2-bundle_2.12:0.11.0"
        }
    ),
    limits=Resources(mem="2000M"),
    cache_version="1",
)
def hudiQery() -> str:
    # if you run in local, you must set SPARK_LOCAL_IP=127.0.0.1. this connection to get jars dependences local file
    spark = flytekit.current_context().spark_session
    # hadoop 3.3.1
    spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.ap-southeast-1.amazonaws.com")
    spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "AKIAZZQUVIBN74RMCUXK")
    spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "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")


    tripsSnapshotDF = spark. \
        read. \
        format("hudi"). \
        load("s3a://hudi-table/logs_mor")

    # tripsSnapshotDF.show()
    pandasDF = tripsSnapshotDF.toPandas()
    firstComitTime = pandasDF['_hoodie_commit_time'][0]
    return firstComitTime

@workflow
def my_query_spark() -> str:
    return hudiQery()

if __name__ == "__main__":
    print(my_query_spark())