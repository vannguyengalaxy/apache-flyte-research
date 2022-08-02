# flyte-project

A template for the recommended layout of a Flyte enabled repository for code written in python using [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Usage (running with your Flyte project )

*** **prerequisites**: make sure the connection with flytectl CLI is working


    ./flytectl_connection.sh

* Step 1: package workflow.


    ./package_workflow.sh.sh -i <IMAGE_NAME> -r <DOCKER_REGISTRY> -v <VERSION>

_example: ./package_workflow.sh.sh -i spark-sql -r ghcr.io/vannguyengalaxy -v v1_

* Step 2: Register workflow using local tgz file.


    flytectl register files --config ~/.flyte/config.yaml  --project <PROJECT_NAME> --domain <DOMAIN_NAME> --archive flyte-package.tgz --version <VERSION>
    

_example: flytectl register files --config ~/.flyte/config.yaml  --project flytesnacks --domain development --archive flyte-package.tgz --version v1_

* Step 3: Open Flyte UI and launch workflow


## NOTE

1. add dependences for test in local
 "spark.jars": "/home/ec2-user/flyte-test/flyte-project/jars/hadoop-aws-3.3.1.jar,"
               "/home/ec2-user/flyte-test/flyte-project/jars/aws-java-sdk-bundle-1.11.375.jar,"
               "/home/ec2-user/flyte-test/flyte-project/jars/hudi-spark3.2-bundle_2.12-0.11.0.jar",
2. if you run in local, you must set SPARK_LOCAL_IP=127.0.0.1. this connection to get jars dependences local file
