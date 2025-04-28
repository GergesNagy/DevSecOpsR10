# Day 6

1. How many Namespaces exist on the system?
```bash
kubectl get ns -A --no-headers | wc -l
```
[!Image](Screenshots/Q1.png)

2. How many pods exist in the `kube-system` namespace?
```bash
kubectl get pods -n kube-system
```
[!Image](Screenshots/Q2.png)

---

3. Create a deployment with:
- Name: `beta`
- Image: `redis`
- Replicas: `2`
- Namespace: `finance`
- Resources Requests:
	- CPU: `5 vCPU`
	- Mem: `1G`
- Resources Limits:
	- CPU: `1 vCPU`
	- Mem: `2G`
a. Create `finance` namespace:
```bash
kubectl create ns finance
```
b. Create a deployment template:
```bash
kubectl create deploy beta \
--image redis \
--replicas 2 \
-n finance \
--dry-run=client -o yaml > my-deploy.yml
```
c. Enter the manifest file and add the resource requirements:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: beta
  name: beta
  namespace: finance
spec:
  replicas: 2
  selector:
    matchLabels:
      app: beta
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: beta
    spec:
      containers:
      - image: redis
        name: redis
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "1"
            memory: "2Gi"
status: {}
```
d. Create the deployment using the manifest file:
```bash
kubectl apply -f my-deploy.yml
```
[!Image](Screenshots/Q3.png)

---

4. How many Nodes exist on the system?
```bash
kubectl get nodes
```

5. Do you see any taints on `master`?
```bash
kubectl describe node controlplane
```
-> None
[!Image](Screenshots/Q5.png)

6. Apply a label `color=blue` to the master node:
```bash
kubectl label node controlplane color=blue
```
[!Image](Screenshots/Q6.png)

7. Create a new deployment named `blue` with the `nginx` image and `3` replicas.
- Set Node Affinity to the deployment to place the pods on `master` only.
- Node Affinity: requiredDuringSchedulingIgnoredDuringExecution
- Key: color
- values: blue
a. Add a label to the required node: (Question 6)
b. Create a deployment template:
```bash
kubectl create deploy blue \
--image nginx \
--replicas 3 \
--dry-run=client -o yaml > my-deploy.yml
```
c. Edit the deployment manifest to add the Node Affinity under the pod's template:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: blue
  name: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: blue
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: blue
    spec:
      containers:
      - image: nginx
        name: nginx
        resources: {}
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: color
                operator: In
                values:
                - blue
status: {}
```
d. Apply the deployment:
```bash
kubectl apply -f my-deploy.yml
```
[!Image](Screenshots/Q7.png)

---
