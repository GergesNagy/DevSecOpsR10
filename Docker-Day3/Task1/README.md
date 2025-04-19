
---
## Task 1
- Python Hello World
- Use the official Python alpine image
- Create a simple Python script that prints "Hello Docker!"
- Make the script run when the container starts

---

```bash
docker build -t py-hello-world .
```
## output
```plaintext
[+] Building 2.2s (8/8) FINISHED                                                                                                       docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                   0.1s
 => => transferring dockerfile: 124B                                                                                                                   0.0s
 => [internal] load metadata for docker.io/library/python:3-alpine                                                                                     1.4s
 => [internal] load .dockerignore                                                                                                                      0.1s
 => => transferring context: 2B                                                                                                                        0.0s
 => [1/3] FROM docker.io/library/python:3-alpine@sha256:18159b2be11db91f84b8f8f655cd860f805dbd9e49a583ddaac8ab39bf4fe1a7                               0.0s
 => [internal] load build context                                                                                                                      0.1s
 => => transferring context: 55B                                                                                                                       0.0s
 => CACHED [2/3] WORKDIR /app                                                                                                                          0.0s
 => [3/3] COPY app.py .                                                                                                                                0.1s
 => exporting to image                                                                                                                                 0.2s
 => => exporting layers                                                                                                                                0.1s
 => => writing image sha256:0bbc9b42614157619af095e459e69b14fec67c7193cdcdb28d80e6b05c126b7a                                                           0.0s
 => => naming to docker.io/library/py-hello-world                                                                                                      0.0s
```

```bash
docker images
```
## output
```plaintext
REPOSITORY                                            TAG       IMAGE ID       CREATED          SIZE
py-hello-world                                        latest    0bbc9b426141   13 seconds ago   44.8MB
```

```bash
docker run py-hello-world 
```
## output

```plaintext
Hello Docker!
```