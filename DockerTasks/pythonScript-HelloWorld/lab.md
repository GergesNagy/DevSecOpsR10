Python Hello World
Use the official Python alpine image
Create a simple Python script that prints "Hello Docker!"
Make the script run when the container start
using a Dockerfile 


[+] Building 4.9s (8/8) FINISHED                                                                                   docker:default
 => [internal] load build definition from Dockerfile                                                                         0.0s
 => => transferring dockerfile: 151B                                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.8.2-alpine                                                       4.1s
 => [internal] load .dockerignore                                                                                            0.0s
 => => transferring context: 2B                                                                                              0.0s
 => CACHED [1/3] FROM docker.io/library/python:3.8.2-alpine@sha256:745fac134e7ea2947934f4baba06db821e63db3607938692017f766c  0.0s
 => [internal] load build context                                                                                            0.0s
 => => transferring context: 35B                                                                                             0.0s
 => [2/3] WORKDIR /app                                                                                                       0.2s
 => [3/3] COPY hello-world.py /app                                                                                           0.1s
 => exporting to image                                                                                                       0.2s
 => => exporting layers                                                                                                      0.1s
 => => writing image sha256:dabe50e27230947a5b2b388f1f5f5ac16bae2e79771c42da2182179a10e73c00                                 0.0s
 => => naming to docker.io/library/hello-docker-script                                                                       0.0s



 ocker run hello-docker-script:latest 
 hello Docker !!