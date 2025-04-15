
---
## Problem 1
- Run the container hello-world
- Check the container status
- Start the stopped container
- Remove the container
- Remove the image

---

```bash
docker run hello-world
```

**Output:**
```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
```

---


```bash
docker ps -a
```

**Output:**
```
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS                      PORTS     NAMES
9644d8ab5b54   hello-world     "/hello"                 10 seconds ago   Exited (0) 9 seconds ago              laughing_sutherland
a150c5e21a48   centos:8        "/bin/bash"              3 weeks ago      Exited (0) 3 weeks ago                amir_nti
6d7eda025887   mongo           "docker-entrypoint.s…"   3 months ago     Exited (0) 3 months ago               1-developing-with-docker-mongodb-1
8cce27e472d8   my-app:1.0      "docker-entrypoint.s…"   3 months ago     Exited (137) 3 months ago             1-developing-with-docker-my-app-1
9392dfd453f5   mongo-express   "/sbin/tini -- /dock…"   3 months ago     Exited (143) 3 months ago             1-developing-with-docker-mongo-express-1
79ec688b7660   5d0da3dc9764    "/bin/bash"              3 months ago     Exited (0) 3 months ago               centosc
```

---


```bash
docker stop 9644
```

**Output:**
```
9644
```

---


```bash
docker start 9644
```

**Output:**
```
9644
```

---


```bash
docker rm 9644
```

**Output:**
```
9644
```

---


```bash
docker images
```

```
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
hello-world       latest    74cc54e27dc4   2 months ago    10.1kB
<none>            <none>    daddd64a4d65   4 months ago    125MB
my-app            1.1       9afc57568926   4 months ago    125MB
alpine            latest    4048db5d3672   4 months ago    7.84MB
my-app            1.0       972d8a572272   4 months ago    125MB
fedora            latest    aa6787b90fe6   5 months ago    158MB
mongo             latest    35c09d23ad5d   5 months ago    854MB
postgres          14.13     480f26a07aa1   8 months ago    422MB
postgres          13.16     9fe2ea8cf50c   8 months ago    419MB
mongo-express     latest    870141b735e7   13 months ago   182MB
centos            7         eeb6ee3f44bd   3 years ago     204MB
centos            8         5d0da3dc9764   3 years ago     231MB
```

---


```bash
docker rmi 74cc
```

**Output:**
```
Untagged: hello-world:latest
Untagged: hello-world@sha256:424f1f86cdf501deb591ace8d14d2f40272617b51b374915a87a2886b2025ece
Deleted: sha256:74cc54e27dc41bb10dc4b2226072d469509f2f22f1a3ce74f4a59661a1d44602
Deleted: sha256:63a41026379f4391a306242eb0b9f26dc3550d863b7fdbb97d899f6eb89efe72
```

---


```bash
docker images
```

**Output:**
```
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
<none>            <none>    daddd64a4d65   4 months ago    125MB
my-app            1.1       9afc57568926   4 months ago    125MB
alpine            latest    4048db5d3672   4 months ago    7.84MB
my-app            1.0       972d8a572272   4 months ago    125MB
fedora            latest    aa6787b90fe6   5 months ago    158MB
mongo             latest    35c09d23ad5d   5 months ago    854MB
postgres          14.13     480f26a07aa1   8 months ago    422MB
postgres          13.16     9fe2ea8cf50c   8 months ago    419MB
mongo-express     latest    870141b735e7   13 months ago   182MB
centos            7         eeb6ee3f44bd   3 years ago     204MB
centos            8         5d0da3dc9764   3 years ago     231MB
```

---
