Multi-stage Build
Create a Dockerfile that:
Uses node image to build a React application
Then copies just the built static files to an nginx image
src/App.js

[+] Building 337.0s (13/13) FINISHED                                                                         docker:default 
 => [internal] load build definition from Dockerfile                                                                   0.0s 
 => => transferring dockerfile: 226B                                                                                   0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine                                                        0.3s
 => [internal] load metadata for docker.io/library/node:18-alpine                                                      0.7s
 => [internal] load .dockerignore                                                                                      0.0s
 => => transferring context: 2B                                                                                        0.0s
 => [builder 1/4] FROM docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a35cb9bc  0.0s
 => [internal] load build context                                                                                      0.0s
 => => transferring context: 346B                                                                                      0.0s
 => [stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:4ff102c5d78d254a6f0da062b3cf39eaf07f01eec0927fd21e219d0a  0.0s
 => CACHED [stage-1 2/3] WORKDIR /usr/share/nginx/html                                                                 0.0s
 => CACHED [builder 2/4] WORKDIR /src                                                                                  0.0s
 => [builder 3/4] COPY .  .                                                                                            0.1s
 => [builder 4/4] RUN npm install                                                                                    334.7s
 => [stage-1 3/3] COPY --from=builder /src/App.js /usr/share/nginx/html                                                0.2s
 => exporting to image                                                                                                 0.2s
 => => exporting layers                                                                                                0.1s
 => => writing image sha256:da8ce6f56b09e4962282c65c86ea795e426b7b28d29b29911c7e10914ef10102                           0.0s
 => => naming to docker.io/library/tes-app                                                                             0.0s

