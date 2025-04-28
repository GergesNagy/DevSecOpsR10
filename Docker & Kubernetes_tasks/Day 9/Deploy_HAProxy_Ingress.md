# HAProxy Ingress Setup

---

## 1. Initialize the Namespace  
Create a namespace called `ingress-namespace-devops`.  
```bash
# Apply the Namespace manifest
kubectl apply -f Manifests/Namespace.yml
```

---

## 2. Service Account Creation  
Create a ServiceAccount named `ingress-sa-devops` within `ingress-namespace-devops`.  
```bash
# Apply the ServiceAccount manifest
kubectl apply -f Manifests/ServiceAccount.yml
```

---

## 3. Define ClusterRole  
Establish a ClusterRole `ingress-cluster-role-devops` granting permissions (`get`, `list`, `watch`, `create`, `patch`, `update`) on resources: ConfigMaps, Secrets, Endpoints, Nodes, Pods, Services, Namespaces, Events, and ServiceAccounts.  
```bash
# Apply the ClusterRole manifest
kubectl apply -f Manifests/ClusterRole.yml
```

---

## 4. Bind the Role to the ServiceAccount  
Create a ClusterRoleBinding `ingress-cluster-rolebinding-devops` in `ingress-namespace-devops`, linking `ingress-cluster-role-devops` to the `ingress-sa-devops` ServiceAccount.  
```bash
# Apply the ClusterRoleBinding manifest
kubectl apply -f Manifests/ClusterRoleBinding.yml
```

---

## 5. Deploy the Default Backend  
Deploy a backend application with one replica in `ingress-namespace-devops`:
- **Deployment Name:** `default-backend-devops`  
- **Label:** `run=ingress-backend`  
- **Container:**  
  - **Name:** `backend-app-container`  
  - **Image:** `gcr.io/google_containers/defaultbackend:1.0`  
  - **Port:** 8080  

```bash
# Apply the Deployment manifest
kubectl apply -f Manifests/Backend-Deployment.yml
```

---

## 6. Expose the Backend Service  
Create a Service named `backend-svc-devops` targeting pods with label `run=ingress-backend`:
- **Port Name:** `backend-port`  
- **Port:** 8080  
- **TargetPort:** 8080  
- **Protocol:** TCP  

```bash
# Apply the Service manifest
kubectl apply -f Manifests/Backend-Service.yml
```

---

## 7. Deploy HAProxy Ingress Controller  
Set up the frontend ingress controller in `ingress-namespace-devops`:
- **Deployment Name:** `ingress-controller-deployment`  
- **ServiceAccount:** `ingress-sa-devops`  
- **Replicas:** 1  
- **Label:** `run=ingress-controller`  
- **Container:**  
  - **Name:** `ingress-app-container`  
  - **Image:** `haproxytech/kubernetes-ingress`  
  - **Args:** `--default-backend-service=ingress-namespace-devops/backend-svc-devops`  
  - **Resources:**  
    - **Requests:** CPU `500m`, Memory `50Mi`  
  - **Probes:**  
    - **Liveness:** HTTP GET `/healthz` on port `1024`  
  - **Ports:**  
    - `http` (80), `https` (443), `stats` (1024)  
  - **Environment Variables:**  
    - `TZ=Etc/UTC`  
    - `POD_NAME` from `metadata.name`  
    - `POD_NAMESPACE` from `metadata.namespace`  

```bash
# Apply the Ingress Controller Deployment
kubectl apply -f Manifests/Frontend-Deployment.yml
```

---

## 8. Expose the Ingress Controller  
Create a NodePort Service `ingress-svc-devops` for pods labeled `run=ingress-controller`:
- **Type:** NodePort  
- **Ports:**  
  - `http`: port 80 → nodePort 32456  
  - `https`: port 443 → nodePort 32567  
  - `stats`: port 1024 → nodePort 32678  

```bash
# Apply the Ingress Service manifest
kubectl apply -f Manifests/Frontend-Service.yml
```
