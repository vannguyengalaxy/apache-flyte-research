# create tempalte config file in path ".flyte/config.yaml"
ADDRESS=$(kubectl -n flyte get ingress|grep flyte-core-grpc |awk '{print $4}')
yes | flytectl config init --host=$ADDRESS

# replace content of config file
cat << EOF > ~/.flyte/config.yaml
admin:
  endpoint: dns:///$(kubectl -n flyte get ingress|grep flyte-core-grpc |awk '{print $4}')
  authType: Pkce
  insecure: false
  insecureSkipVerify: true
logger:
  show-source: true
  level: 0
EOF