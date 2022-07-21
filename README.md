# flyte-project

A template for the recommended layout of a Flyte enabled repository for code written in python using [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Usage

To get up and running with your Flyte project, we recommend following the
[Flyte getting started guide](https://docs.flyte.org/en/latest/getting_started.html).


## NOTE
1. This APP name is also added to ``docker_build_and_tag.sh`` - ``APP_NAME``
2. We recommend using a git repository and this the ``docker_build_and_tag.sh``
   to build your docker images
3. We also recommend using pip-compile to build your requirements.

note:
1. add dependences for test in local
 "spark.jars": "/home/ec2-user/flyte-test/flyte-project/jars/hadoop-aws-3.3.1.jar,"
               "/home/ec2-user/flyte-test/flyte-project/jars/aws-java-sdk-bundle-1.11.375.jar,"
               "/home/ec2-user/flyte-test/flyte-project/jars/hudi-spark3.2-bundle_2.12-0.11.0.jar",