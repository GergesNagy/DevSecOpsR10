# Day 6 Exercises

---

## 1. Count all Namespaces in the cluster  
```bash
kubectl get ns -A --no-headers | wc -l
```  
![Total Namespaces](Screenshots/Q1.png)

---

## 2. List all Pods in the `kube-system` namespace  
```bash
kubectl get pods -n kube-system
```  
![kube-system Pods](Screenshots/Q2.png)

---

## 3. Deploy Redis as `beta` in the `finance` namespace

**Requirements:**  
- **Name:** `beta`  
- **Image:** `redis`  
- **Replicas:** `2`  
- **Namespace:** `finance`  
- **Resource Requests:**  
  - CPU: 5 vCPU  
  - Memory: 1 Gi  
- **Resource Limits:**  
  - CPU: 1 vCPU  
  - Memory: 2 Gi  

1. **Create the namespace**  
   ```bash
   kubectl create namespace finance
   ```

2. **Generate a deployment manifest**  
   ```bash
   kubectl create deployment beta      --image=redis      --replicas=2      -n finance      --dry-run=client -o yaml > beta-deploy.yml
   ```

3. **Edit `beta-deploy.yml` to include resources**  
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: beta
     namespace: finance
     labels:
       app: beta
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: beta
     template:
       metadata:
         labels:
           app: beta
       spec:
         containers:
         - name: redis
           image: redis
           resources:
             requests:
               cpu: "500m"
               memory: "1Gi"
             limits:
               cpu: "1"
               memory: "2Gi"
   ```

4. **Apply the manifest**  
   ```bash
   kubectl apply -f beta-deploy.yml
   ```  
   ![Deployment beta](Screenshots/Q3.png)

---

## 4. Check how many Nodes are in the cluster  
```bash
kubectl get nodes
```

---

## 5. Inspect `controlplane` for taints  
```bash
kubectl describe node controlplane
```  
> **Result:** None  
![No taints](Screenshots/Q5.png)

---

## 6. Label the master node with `color=blue`  
```bash
kubectl label node controlplane color=blue
```  
![Master labeled](Screenshots/Q6.png)

---

## 7. Deploy NGINX as `blue` only on the labeled master

**Requirements:**  
- **Name:** `blue`  
- **Image:** `nginx`  
- **Replicas:** `3`  
- **Node Affinity:**  
  - **Type:** `requiredDuringSchedulingIgnoredDuringExecution`  
  - **Key:** `color`  
  - **Value:** `blue`

1. **(Already done)** Label the master node (`color=blue`)  
2. **Generate a deployment manifest**  
   ```bash
   kubectl create deployment blue      --image=nginx      --replicas=3      --dry-run=client -o yaml > blue-deploy.yml
   ```

3. **Add Node Affinity to `blue-deploy.yml`**  
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: blue
     labels:
       app: blue
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: blue
     template:
       metadata:
         labels:
           app: blue
       spec:
         containers:
         - name: nginx
           image: nginx
         affinity:
           nodeAffinity:
             requiredDuringSchedulingIgnoredDuringExecution:
               nodeSelectorTerms:
               - matchExpressions:
                 - key: color
                   operator: In
                   values:
                   - blue
   ```

4. **Apply the manifest**  
   ```bash
   kubectl apply -f blue-deploy.yml
   ```  
   ![Deployment blue](Screenshots/Q7.png)
