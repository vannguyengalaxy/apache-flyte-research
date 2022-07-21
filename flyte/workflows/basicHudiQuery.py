from flytekit import Resources, task, workflow, kwtypes
from flytekitplugins.spark import Spark
import flytekit
from typing import Dict
@task(
    task_config=Spark(
        # this configuration is applied to the spark cluster
        spark_conf={
            "spark.driver.memory": "1000M",
            "spark.executor.memory": "1000M",
            "spark.executor.cores": "1",
            "spark.executor.instances": "1",
            "spark.driver.cores": "1",
            "spark.jars": "local:///root/jars/hadoop-aws-3.3.1.jar,"
                          "local:///root/jars/aws-java-sdk-bundle-1.11.375.jar,"
                          "local:///root/jars/hudi-spark3.2-bundle_2.12-0.11.0.jar",
            "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
            "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.hudi.catalog.HoodieCatalog",
            "spark.sql.extensions": "org.apache.spark.sql.hudi.HoodieSparkSessionExtension"

        }
    ),
    limits=Resources(mem="2000M"),
    cache_version="1",
)
def hudiQery() -> Dict[str, str]:
    # if you run in local, you must set SPARK_LOCAL_IP=127.0.0.1. this connection to get jars dependences local file
    spark = flytekit.current_context().spark_session
    # hadoop 3.3.1
    spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.ap-southeast-1.amazonaws.com")
    spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "AKIAZZQUVIBN74RMCUXK")
    spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "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")

    df = spark.read.format('org.apache.hudi').load('s3a://hudi-table/logs_mor' + '/*/*')

    return df.select("_hoodie_commit_time").collect()[0].asDict()

@workflow
def my_query_spark() -> Dict[str, str]:
    return hudiQery()

if __name__ == "__main__":
    print(my_query_spark())