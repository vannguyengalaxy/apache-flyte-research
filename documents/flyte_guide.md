## 1. Deployment
### 1.1. Flyte sandbox (locally)

#### 1.1.1. Install flytectl by shell script and set environment path**

    curl -sL https://ctl.flyte.org/install | bash
    export PATH=$HOME/bin:$PATH

#### 1.1.2. create cluster
* step 1. start flyte sandbox cluster 
 
      start sandbox by flytectl

* step 2: set env path for kube config and flytectl config 
    *Note: you can copy this variable in logs console after sandbox start.* 

       export KUBECONFIG=$KUBECONFIG:/<path_to>/.kube/config:/<path>/.flyte/k3s/k3s.yaml
       export FLYTECTL_CONFIG=/<path_to>/.flyte/config-sandbox.yaml

* Step 3: Open this url (http://localhost:30081/console) on your browser.**
### 1.2. Flyte Native (AWS)

#### 1.2.1. Deploy cluster 
reference: [read in more detail](https://docs.flyte.org/en/latest/deployment/aws/manual.html#deployment-aws-manual)

#### 1.2.2. Setup connection to flytectl CLI
step 1: Install flytectl [(1.1.1)](####-1.1.1.-Install-flytectl-by-shell-script-and-set-environment-path)

step 2: generate config file   
  
    flytectl config init --host=k8s-flyte-517d5d45e2-578377867.ap-southeast-1.elb.amazonaws.com --insecure


step 3: Get flyteadmin host and modify in flyte config file

    nano ~/.flyte/config.yaml
   
step 4: Use below config:
 
    admin:
      endpoint: dns:///k8s-flyte-517d5d45e2-578377867.ap-southeast-1.elb.amazonaws.com
      authType: Pkce
      insecure: false
      insecureSkipVerify: true
    logger:
      show-source: true
      level: 0


## 2. Setup a project
* Prerequisites: make sure you have git and python >=3.7

Step 1: Create virtual environment

    python -m venv ~/venvs/flyte
    source ~/venvs/flyte/bin/activate
Step 2: Instal flytekit on it.

    pip install flytekit
Step 3: create project

    pyflyte  init  <project_name>
Then, the project directory will be created with a sample workflow. More instructions can be found in [this link](https://docs.flyte.org/projects/cookbook/en/stable/auto/larger_apps/larger_apps_setup.html)

## 3. Register workflow
Step 1: Build image

    ./docker_build_and_tag.sh -a <image_name> -r <docker_registry> -v <version>

*example: ./docker_build_and_tag.sh -a flyte-example-pyspark-pi -r ghcr.io/vannguyengalaxy -v v1*

Step 2: Package workflow

    pyflyte --pkgs flyte.workflows package --image "<image_name>:<version>"

*example: pyflyte --pkgs flyte.workflows package --image "ghcr.io/vannguyengalaxy/flyte-hudi-query:v1"*

Step 3: Push image to docker registry

    docker push <image_name>:<version>

step 4: Upload package to the Flyte backend *(Note: make sure the image publicly accessible)*


    flytectl register files --project <project_name> --domain <domain_name> --archive flyte-package.tgz --version <version>
  
  *example: flytectl register files --project flytesnacks --domain development --archive flyte-package.tgz --version v1*

## 4. scheduler workflow
reference: [read in more detail](https://docs.flyte.org/projects/cookbook/en/stable/auto/core/scheduled_workflows/lp_schedules.html#fixed-rate-intervals)


## 3. Troubleshooting
### 3.1. scheduler workflow on flyte sandbox on local
Scheduler pod can not be pre-installed in localy Flyte Sandbox, so we can manual install scheduler pod to run scheduler job.
Step 1: adding below config to [values-sandbox.yml](https://github.com/flyteorg/flyte/blob/master/charts/flyte-core/values-sandbox.yaml)

    workflow_scheduler:
      enabled: true
      type: native

Step 2: upgrade helm 

    helm upgrade -f values-sandbox.yaml flyte-core flyte/flyte-core --version v1.0.2 -n flyte


