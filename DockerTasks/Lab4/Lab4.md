```bash
a docker run -dit --name apache httpd
844474f856999eeca4ab19dad33cec6a05a5b8553a6b862c5da5d45d0678bfef
- ls $(pwd)
index.html
- docker cp $(pwd)/index.html apache:/usr/local/apache2/htdocs/index.html
Successfully copied 2.56kB to apache:/usr/local/apache2/htdocs/index.html
- curl http://localhost:8080
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
- docker commit apache my-apache
sha256:2d318e3feb9fa7987241c14f0e0c01d9baa51c8ae0d08e14695e6a8da7de8ff1
- docker ps 
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS                  NAMES
268a4782a38c   httpd     "httpd-foreground"   21 minutes ago   Up 21 minutes   0.0.0.0:8080->80/tcp   apache
- docker images
REPOSITORY                                            TAG       IMAGE ID       CREATED         SIZE
my-apache                                             latest    2d318e3feb9f   5 minutes ago   148MB
httpd                                                 latest    10fd72f437c4   2 months ago    148MB

```
---

```bash
amir@amir-ubuntu:/media/amir/Hard_HDD/DevOps/NTI/Technical/Docker/Docker/Lab4$ docker build -t my_custom_apache .
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

amir@amir-ubuntu:/media/amir/Hard_HDD/DevOps/NTI/Technical/Docker/Docker/Lab4$ docker build -t my_custom_apache .
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


```