# Day 8 Labs

---

## 1. List all ConfigMaps in the cluster  
```bash
kubectl get configmap --all-namespaces
```  

---

## 2. Create a new ConfigMap named `site-settings-cm` with `APP_THEME=darkblue`  
```bash
kubectl create configmap site-settings-cm --from-literal=APP_THEME=darkblue
```  

---

## 3. Launch a Pod `theme-viewer` using the `nginx` image and inject the ConfigMap  
a. Generate a Pod manifest template:  
```bash
kubectl run theme-viewer --image=nginx --dry-run=client -o yaml > theme-viewer-pod.yml
```  
b. Edit `theme-viewer-pod.yml` to include the environment variable:  
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: theme-viewer
  labels:
    app: theme-viewer
spec:
  containers:
  - name: theme-viewer
    image: nginx
    env:
    - name: APP_THEME
      valueFrom:
        configMapKeyRef:
          name: site-settings-cm
          key: APP_THEME
  restartPolicy: Always
```  
c. Apply the Pod manifest:  
```bash
kubectl apply -f theme-viewer-pod.yml
```  

---

## 4. Count all Secrets in the cluster  
```bash
kubectl get secret --all-namespaces
```  
![Image](Screenshots/Q4.png)

---

## 5. Inspect the keys in the `default-token` Secret  
```bash
kubectl describe secret default-token-xxxxx -n default
```  
![Image](Screenshots/Q5.png)

---

## 6. Create a Pod `database-pod` with the `mysql:5.7` image  
```bash
kubectl run database-pod --image=mysql:5.7 --dry-run=client -o yaml > database-pod.yml
kubectl apply -f database-pod.yml
```  
![Image](Screenshots/Q6.png)

---

## 7. Explain why `database-pod` is not Ready  
The container needs the `MYSQL_ROOT_PASSWORD` environment variable to be set.  
![Image](Screenshots/Q7.png)

---

## 8. Create a Secret `database-credentials` with multiple keys  
```bash
kubectl create secret generic database-credentials   --from-literal=MYSQL_DATABASE=sql01   --from-literal=MYSQL_USER=user1   --from-literal=MYSQL_PASSWORD=password   --from-literal=MYSQL_ROOT_PASSWORD=password123
```  

---

## 9. Attach the Secret to `database-pod` as environment variables  
a. Edit the Pod (fails and saves to `/tmp`):  
```bash
kubectl edit pod database-pod
```  
b. Under `containers[0]`, add:  
```yaml
envFrom:
- secretRef:
    name: database-credentials
```  
c. Replace the Pod:  
```bash
kubectl replace --force -f /tmp/kubectl-edit-*.yaml
```  

---

## 10. Create a multi-container Pod `multi-demo-pod`  
- **Container 1:** `alpha` (image: busybox, command: `sleep 3600`)  
- **Container 2:** `beta` (image: redis)

a. Generate template:  
```bash
kubectl run multi-demo-pod --image=busybox --dry-run=client -o yaml > multi-pod.yml
```  
b. Edit `multi-pod.yml` to include both containers:  
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-demo-pod
spec:
  containers:
  - name: alpha
    image: busybox
    command: ["sleep", "3600"]
  - name: beta
    image: redis
  restartPolicy: Always
```  
c. Apply it:  
```bash
kubectl apply -f multi-pod.yml
```  
![Image](Screenshots/Q10.png)

---

## 11. Create a Pod `init-demo-pod` with an initContainer  
- **Init Container:** busybox, command: `sleep 20`  
- **Main Container:** redis

a. Generate template:  
```bash
kubectl run init-demo-pod --image=redis --dry-run=client -o yaml > init-pod.yml
```  
b. Edit `init-pod.yml`:  
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-demo-pod
spec:
  initContainers:
  - name: wait-init
    image: busybox
    command: ["sleep", "20"]
  containers:
  - name: redis
    image: redis
  restartPolicy: Always
```  
c. Apply it:  
```bash
kubectl apply -f init-pod.yml
```  
![Image](Screenshots/Q11.png)

---

## 12. Pod to print environment variables `env-printer-pod`  
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-printer-pod
spec:
  containers:
  - name: printer-container
    image: bash
    env:
    - name: MSG_GREETING
      value: "Welcome to"
    - name: ORG_NAME
      value: "DevOps"
    - name: TEAM_NAME
      value: "Industries"
    command: ["echo", "$(MSG_GREETING) $(ORG_NAME) $(TEAM_NAME)"]
  restartPolicy: Never
```  
View logs with:  
```bash
kubectl logs -f env-printer-pod
```  
![Image](Screenshots/Q12.png)

---

## 13. Locate the default kubeconfig file  
Typically at `~/.kube/config`  
![Image](Screenshots/Q13.png)

---

## 14. Determine how many clusters are defined  
There is **1** cluster listed in the default kubeconfig.  
![Image](Screenshots/Q14.png)

---

## 15. Identify the user in the current context  
The configured user is `system:node:controlplane`.

---

## 16. Define a PersistentVolume `pv-storage`  
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-storage
spec:
  storageClassName: lesson-storage
  capacity:
    storage: 100Mi
  accessModes:
  - ReadWriteMany
  hostPath:
    path: "/mnt/data"
  persistentVolumeReclaimPolicy: Retain
```  
![Image](Screenshots/Q16.png)

---

## 17. Create a PersistentVolumeClaim `claim-storage-1`  
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: claim-storage-1
spec:
  storageClassName: lesson-storage
  volumeName: pv-storage
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 50Mi
```  
![Image](Screenshots/Q17.png)

---

## 18. Launch a Pod `storage-demo-pod` using the PVC  
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-demo-pod
spec:
  volumes:
  - name: log-volume
    persistentVolumeClaim:
      claimName: claim-storage-1
  containers:
  - name: web-server
    image: nginx
    volumeMounts:
    - name: log-volume
      mountPath: "/var/log/nginx"
```  
