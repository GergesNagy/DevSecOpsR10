
---
## Problem 2
- Run container centos or ubuntu in an interactive mode
- Run the following command in the container “echo docker ”
- Open a bash shell in the container and touch a file named hello-docker
- Stop the container and remove it. Write your comment about the file hello-docker
- Remove all stopped containers

---

```bash
docker run -it centos:8 bash
```
**Output:**
```bash
[root@01a8884df697 /]# echo docker
docker
[root@01a8884df697 /]# touch hello-docker
[root@01a8884df697 /]# exit
exit
```
---

```bash
docker ps -a
```
**Output:**
```
CONTAINER ID   IMAGE           COMMAND       CREATED          STATUS                      PORTS     NAMES
01a8884df697   centos:8        "/bin/bash"   52 seconds ago   Exited (0) 5 seconds ago              pensive_knuth
```
---

```bash
docker stop 01a888
```
**Output:**
```
01a888
```

```bash
docker rm 01a888
```
**Output:**
```
01a888
```

```bash
docker ps -a
```
**Output:**
```
CONTAINER ID   IMAGE     COMMAND     CREATED     STATUS     PORTS     NAMES
```
---

```bash
docker container prune
```
**Output:**
```
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
a150c5e21a481678382996477122a31dca8acf8fd4bbddff73723ed53831de66
6d7eda02588745a33e0f9659fa740e4be9e88aee6a63c6944687ddae1342cbb4
8cce27e472d8e5def0789f7914f32bd83fe397dd4b2c9652f6bd560d994f6b87
9392dfd453f575304fea95f16e5cecc7f0789546b15c93e6a6ec701d83b50299
79ec688b76607bfe0f68315ec385a803fcc7b5c1ea31e995700d8b3f63d5c674

Total reclaimed space: 296.8kB
```
--- 

