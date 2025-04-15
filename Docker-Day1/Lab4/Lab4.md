
---
## Problem 4
- Run the image httpd again without attaching any 
volumes
- Add html static files to the container and make 
sure they are accessible
- Commit the container with image name 
IMAGE_NAME
- Create a dockerfile for the previous image and 
build the image from this dockerfile

---

```bash
docker run -dit --name apache httpd
```
**Output:**
```
844474f856999eeca4ab19dad33cec6a05a5b8553a6b862c5da5d45d0678bfef
```

```bash
ls /home/amir/Desktop/StaticWebSite/
```
**Output:**
```
index.html
```

```bash
docker cp /home/amir/Desktop/StaticWebSite/index.html apache:/usr/local/apache2/htdocs/index.html
```
**Output:**
```
Successfully copied 2.56kB to apache:/usr/local/apache2/htdocs/index.html
```

```bash
curl http://localhost:8080
```
**Output:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello to Docker</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Hello to Docker</h1>
</body>
</html>
```

---

```bash
docker commit apache my-apache
```
**Output:**
```
sha256:2d318e3feb9fa7987241c14f0e0c01d9baa51c8ae0d08e14695e6a8da7de8ff1
```

```bash
docker ps 
```
**Output:**
```
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS                  NAMES
268a4782a38c   httpd     "httpd-foreground"   21 minutes ago   Up 21 minutes   0.0.0.0:8080->80/tcp   apache
```

```bash
docker images
```
**Output:**
```
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
my-apache     latest    2d318e3feb9f   5 minutes ago   148MB
httpd         latest    10fd72f437c4   2 months ago    148MB
```

---

```bash
amir@amir-ubuntu:/media/amir/Hard_HDD/DevOps/NTI/Technical/Docker/Docker/Lab4$ docker build -t my_custom_apache .
```
**Output:**
```
[+] Building 0.2s (7/7) FINISHED                                                                          docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 93B                                                                                       0.0s
 => [internal] load metadata for docker.io/library/httpd:latest                                                           0.0s
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [internal] load build context                                                                                         0.0s
 => => transferring context: 32B                                                                                          0.0s
 => [1/2] FROM docker.io/library/httpd:latest                                                                             0.0s
 => CACHED [2/2] COPY index.html /usr/local/apache2/htdocs/                                                               0.0s
 => exporting to image                                                                                                    0.0s
 => => exporting layers                                                                                                   0.0s
 => => writing image sha256:397e3d57c005840e0275c1ddd7ccf36173fa696bd2fc2a7cf6d465ab2e67637f                              0.0s
 => => naming to docker.io/library/my_custom_apache                                                                       0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/egjukhb9aczgqet7xnsb5gzhz

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview 
```

```bash
amir@amir-ubuntu:/media/amir/Hard_HDD/DevOps/NTI/Technical/Docker/Docker/Lab4$ docker run -d -p 8080:80 my_custom_apache:latest 
```
**Output:**
```
a9759136d3677283112ffb581491047282779a581788001efc410ac9a41c0889
```

---
