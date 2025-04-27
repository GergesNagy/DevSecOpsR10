#!/bin/bash

set -e

apply_and_wait() {
    echo "Creating $1 ..."
    kubectl create -f "$1"

    # Extract kind and name
    KIND=$(grep -m1 '^kind:' "$1" | awk '{print $2}')
    NAME=$(grep -m1 '^  name:' "$1" | awk '{print $2}')
    NAMESPACE=$(grep -m1 '^  namespace:' "$1" | awk '{print $2}')

    # Default namespace if not found
    if [ -z "$NAMESPACE" ]; then
        NAMESPACE="default"
    fi

    # Wait logic based on KIND
    case "$KIND" in
        Deployment)
            echo "Waiting for deployment $NAME to be available..."
            kubectl rollout status deployment/"$NAME" -n "$NAMESPACE"
            ;;
        ServiceAccount|ClusterRole|ClusterRoleBinding|Namespace|Service)
            echo "$KIND $NAME created, no need to wait."
            ;;
        *)
            echo "Unknown kind $KIND, skipping wait."
            ;;
    esac

    echo "$KIND $NAME is ready."
    echo "---------------------------------------"
}

# List of YAML files in order
yamls=(
    namespace.yaml
    serviceAccount.yaml
    clusterRole.yaml
    clusterRoleBinding.yaml
    deploymentBackend.yaml
    serviceBackend.yaml
    deploymentFrontend.yaml
    serviceFrontend.yaml
)

for yaml in "${yamls[@]}"; do
    apply_and_wait "$yaml"
done

echo "All resources created successfully!"
