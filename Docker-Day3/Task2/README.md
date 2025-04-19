
---
##  Task 2
- Create a Dockerfile that:
- Uses node image to build a React application
- Then copies just the built static files to an nginx image

---

## Build the Docker Image

```bash
docker build -t multi-stage .
```

### Output

```plaintext
[+] Building 4.2s (16/16) FINISHED                                                                                                                                            docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                          0.1s
 => => transferring dockerfile: 603B                                                                                                                                                          0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine                                                                                                                               3.8s
 => [internal] load metadata for docker.io/library/node:18                                                                                                                                    3.7s
 => [internal] load .dockerignore                                                                                                                                                             0.1s
 => => transferring context: 2B                                                                                                                                                               0.0s
 => [build 1/7] FROM docker.io/library/node:18@sha256:df9fa4e0e39c9b97e30240b5bb1d99bdb861573a82002b2c52ac7d6b8d6d773e                                                                        0.0s
 => [stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10                                                                 0.0s
 => [internal] load build context                                                                                                                                                             0.1s
 => => transferring context: 182B                                                                                                                                                             0.0s
 => CACHED [stage-1 2/3] RUN rm -rf /usr/share/nginx/html/*                                                                                                                                   0.0s
 => CACHED [build 2/7] WORKDIR /app                                                                                                                                                           0.0s
 => CACHED [build 3/7] COPY package.json ./                                                                                                                                                   0.0s
 => CACHED [build 4/7] RUN npm install                                                                                                                                                        0.0s
 => CACHED [build 5/7] COPY public ./public                                                                                                                                                   0.0s
 => CACHED [build 6/7] COPY src ./src                                                                                                                                                         0.0s
 => CACHED [build 7/7] RUN npm run build                                                                                                                                                      0.0s
 => CACHED [stage-1 3/3] COPY --from=build /app/build /usr/share/nginx/html                                                                                                                   0.0s
 => exporting to image                                                                                                                                                                        0.0s
 => => exporting layers                                                                                                                                                                       0.0s
 => => writing image sha256:2cdb8e1883a82b759785e98750551d0b3c013e61f95ca90f65da0b75b2a6c0be                                                                                                  0.0s
 => => naming to docker.io/library/multi-stage                                                                                                                                                0.0s
```

---

##  Step 3: Run the Container

```bash
docker run --name react-app -p 8080:80 multi-stage
```

### Output

```plaintext
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/04/17 18:15:46 [notice] 1#1: using the "epoll" event method
2025/04/17 18:15:46 [notice] 1#1: nginx/1.27.5
2025/04/17 18:15:46 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/04/17 18:15:46 [notice] 1#1: OS: Linux 6.10.0-linuxkit
2025/04/17 18:15:46 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/04/17 18:15:46 [notice] 1#1: start worker processes
2025/04/17 18:15:46 [notice] 1#1: start worker process 30
2025/04/17 18:15:46 [notice] 1#1: start worker process 31
2025/04/17 18:15:46 [notice] 1#1: start worker process 32
2025/04/17 18:15:46 [notice] 1#1: start worker process 33
2025/04/17 18:15:46 [notice] 1#1: start worker process 34
2025/04/17 18:15:46 [notice] 1#1: start worker process 35
2025/04/17 18:15:46 [notice] 1#1: start worker process 36
2025/04/17 18:15:46 [notice] 1#1: start worker process 37
172.17.0.1 - - [17/Apr/2025:18:20:10 +0000] "GET / HTTP/1.1" 200 207 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [17/Apr/2025:18:20:10 +0000] "GET /static/js/main.6d54140b.js HTTP/1.1" 200 141300 "http://localhost:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [17/Apr/2025:18:20:11 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36" "-"
2025/04/17 18:20:11 [error] 30#30: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
2025/04/17 18:20:24 [notice] 1#1: signal 28 (SIGWINCH) received
2025/04/17 18:20:25 [notice] 1#1: signal 28 (SIGWINCH) received
2025/04/17 18:20:25 [notice] 1#1: signal 28 (SIGWINCH) received
2025/04/17 18:20:25 [notice] 1#1: signal 28 (SIGWINCH) received
2025/04/17 18:20:26 [notice] 1#1: signal 28 (SIGWINCH) received
```

---

## Open in Browser

Visit [http://localhost:8080](http://localhost:8080) to view your React app served by nginx.

### App Successfully Loaded

![React App Validation](react-app-validation.png)


---
