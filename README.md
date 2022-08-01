# flyte-project

A template for the recommended layout of a Flyte enabled repository for code written in python using [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Usage

* running with your Flyte project
Step 1: stet up connection with flytectl CLI

`flytectl_connection.sh`

Step 2: Register workflow using local tgz file.

`./register_workflow.sh -i <IMAGE_NAME> -r <DOCKER_REGISTRY> -v <VERSION> `

_example: ./register_workflow.sh -i spark-sql -r ghcr.io/vannguyengalaxy -v v1_

## NOTE

1. add dependences for test in local
 "spark.jars": "/home/ec2-user/flyte-test/flyte-project/jars/hadoop-aws-3.3.1.jar,"
               "/home/ec2-user/flyte-test/flyte-project/jars/aws-java-sdk-bundle-1.11.375.jar,"
               "/home/ec2-user/flyte-test/flyte-project/jars/hudi-spark3.2-bundle_2.12-0.11.0.jar",
2. if you run in local, you must set SPARK_LOCAL_IP=127.0.0.1. this connection to get jars dependences local file
