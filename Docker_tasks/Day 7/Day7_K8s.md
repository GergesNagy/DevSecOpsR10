# Day 7 Tasks

---

## 1. Count all DaemonSets across every namespace  
```bash
kubectl get daemonsets --all-namespaces
```  

---

## 2. List the DaemonSets in the `kube-system` namespace  
```bash
kubectl get daemonsets -n kube-system
```  

---

## 3. Find the container image used by the Pod managed by the `kube-proxy` DaemonSet  
![DaemonSet Pod Image](Screenshots/Q3.png)

---

## 4. Deploy a FluentD DaemonSet named `fluent-logger` in `kube-system`

a. Generate a Deployment manifest as a template:  
```bash
kubectl create deployment fluent-logger   -n kube-system   --image=k8s.gcr.io/fluentd-elasticsearch:1.20   --dry-run=client -o yaml > fluentd-ds.yaml
```

b. Edit `fluentd-ds.yaml` to convert it into a DaemonSet:  
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-logger
  namespace: kube-system
  labels:
    component: fluent-logger
spec:
  selector:
    matchLabels:
      component: fluent-logger
  template:
    metadata:
      labels:
        component: fluent-logger
    spec:
      containers:
      - name: fluentd
        image: k8s.gcr.io/fluentd-elasticsearch:1.20
        resources: {}
```

c. Apply the DaemonSet manifest:  
```bash
kubectl apply -f fluentd-ds.yaml
```  
![FluentD DaemonSet Deployed](Screenshots/Q4.png)

---

## 5. Launch a Pod called `backend-pod` with `nginx:alpine` and label it `tier=backend`  
```bash
kubectl run backend-pod --image=nginx:alpine --labels="tier=backend"
```

---

## 6. Start a Pod named `test-client` using `nginx:alpine`  
```bash
kubectl run test-client --image=nginx:alpine
```

---

## 7. Expose the `backend-pod` as a Service named `backend-svc` on port 80  
```bash
kubectl expose pod backend-pod --name=backend-svc --port=80
```

---

## 8. From within `test-client`, curl the `backend-svc`. What response do you get?  
![Curl Response](Screenshots/Q8.png)

---

## 9. Create a Deployment named `frontend-app` with 2 replicas of `nginx`  
```bash
kubectl create deployment frontend-app --image=nginx --replicas=2
```

---

## 10. Expose `frontend-app` as a NodePort Service `frontend-svc` on port 80 and nodePort 30082

a. Generate a Service manifest:  
```bash
kubectl expose deployment frontend-app   --name=frontend-svc   --type=NodePort   --port=80   --dry-run=client -o yaml > frontend-svc.yaml
```

b. Edit `frontend-svc.yaml` to include the NodePort:  
```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-svc
  labels:
    app: frontend-app
spec:
  type: NodePort
  selector:
    app: frontend-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30082
```

c. Apply the Service manifest:  
```bash
kubectl apply -f frontend-svc.yaml
```

---

## 11. Retrieve the Node IP and access the service  
```bash
kubectl get nodes -o wide
curl http://<NODE_IP>:30082
```  
![Access Frontend](Screenshots/Q11.png)

---

## 12. Display the total count of static Pods in the cluster  
![Static Pods Count](Screenshots/Q12.png)

---

## 13. Identify which node hosts the static Pods  
> controlplane  
![Static Pods Node](Screenshots/Q13.png)
