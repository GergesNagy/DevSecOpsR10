# Lab1 – Pods

## Day 5

### 1. How many pods exist on the system?
**Answer:** Zero pods exist

![1](screenshots/1.png)
### 2. How many Nodes exist on the system?
**Answer:** 2 nodes exist

![2](screenshots/2.png)

### 3. Create a new pod with the nginx image.
**Image name:** `nginx`

![3](screenshots/3.png)

### 4. Which nodes are these pods placed on?

![4](screenshots/4.png)

### 5. Create pod from the below YAML using `kubectl apply`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp
  namespace: default
spec:
  containers:
    - image: nginx
      imagePullPolicy: Always
      name: nginx
    - image: agentx
      imagePullPolicy: Always
      name: agentx
```


![5](screenshots/5.png)



### 6. How many containers are part of the pod `webapp`?
**Answer:** 2 containers

### 7. What images are used in the new `webapp` pod?
**Answer:** `nginx`, `agentx` (but it is not pulled)

### 8. What is the state of the container `agentx` in the pod `webapp`?
**Answer:** state: Waiting, reason: ImagePullBackOff

### 9. Why do you think the container `agentx` in pod `webapp` is in error?
**Answer:** Repository does not exist

### 10. Delete the `webapp` Pod.

![10](screenshots/10.png)

### 11. Create a new pod with the name `redis` and with the image `redis123`.
- **Name:** `redis`
- **Image Name:** `redis123`

![11](screenshots/11.png)

### 12. Now change the image on this pod to `redis`. Once done, the pod should be in a running state.

![12](screenshots/12.png)

### 13. Create a pod called `my-pod` of image `nginx:alpine`.

![13](screenshots/13.png)

### 14. Delete the pod called `my-pod`.

![14](screenshots/14.png)
