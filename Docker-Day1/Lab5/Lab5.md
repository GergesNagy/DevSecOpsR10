
---
## Problem 5
- Create a volume called mysql_data, then deploy a MySQL database called app-database. 
- Use the mysql latest image, and use the -e flag to set MYSQL_ROOT_PASSWORD to P4sSw0rd0!.
- Mount the mysql_data volume to /var/lib/mysql. 
- The container should run in the background.

---
```bash
amir@amir-ubuntu:~$ docker volume create mysql_data 
```
**Output:**
```text
mysql_data
```

---

```bash
amir@amir-ubuntu:~$ docker volume ls | grep mysql
```
**Output:**
```text
local     mysql_data
```

---

```bash
amir@amir-ubuntu:~$ docker run -dit \
  --name app-database \
  -e MYSQL_ROOT_PASSWORD=P4sSw0rd0\! \
  -v mysql_data:/var/lib/mysql \
  mysql:latest
```
**Output:**
```text
Unable to find image 'mysql:latest' locally
latest: Pulling from library/mysql
cea172a6e83b: Pull complete 
daac2c594bdd: Pull complete 
cb8acbf2440c: Pull complete 
fae51f7de1fb: Pull complete 
b2ead3e96e6b: Pull complete 
769c3ac51f88: Pull complete 
79f239a40e62: Pull complete 
c11056354384: Pull complete 
49978e7ccddf: Pull complete 
548990e33276: Pull complete 
Digest: sha256:0596fa224cdf3b3355ce3ddbfd7ce77be27ec9e51841dfc5d2e1c8b81eea69d2
Status: Downloaded newer image for mysql:latest
dd84e061fa4df5434d5fe0ca4be2e3d1ff718ba74f696fd589ec11998d4e6279
```

---

```bash
amir@amir-ubuntu:~$ docker ps
```
**Output:**
```text
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                  NAMES
dd84e061fa4d   mysql:latest              "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    3306/tcp, 33060/tcp    app-database
a9759136d367   my_custom_apache:latest   "httpd-foreground"       12 minutes ago   Up 12 minutes   0.0.0.0:8080->80/tcp   youthful_hypatia
```

---

```bash
amir@amir-ubuntu:~$ docker volume inspect mysql_data
```
**Output:**
```json
[
    {
        "CreatedAt": "2025-04-14T23:22:09Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/mysql_data/_data",
        "Name": "mysql_data",
        "Options": null,
        "Scope": "local"
    }
]
```

---
