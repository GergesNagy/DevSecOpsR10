```bash
docker run -d --name apache -v /home/amir/Desktop/StaticWebSite:/usr/local/apache2/htdocs  httpd
```
bd8b8ba71e4909acd6c4b8947a35c4ebfc1dae8f360ef5e0709d891fa9bf3b98
---
```bash
docker stop apache
```
apache
```bash
docker rm apache
```
apache
---
```bash
docker run -d --name apache -v /home/amir/Desktop/StaticWebSite:/usr/local/apache2/htdocs -p 9898:80 httpd
```
02952b50865d819d103ca3506578a0505e4c8807450fa0538f54baa3d381fc94
```bash
docker exec -it apache bash

root@02952b50865d:/usr/local/apache2# ls -l /usr/local/apache2/htdocs
total 4
-rwxrwxrwx 1 root root 566 Apr 14 15:49 index.html
root@02952b50865d:/usr/local/apache2# cat /usr/local/apache2/htdocs/index.html
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


root@02952b50865d:/usr/local/apache2# exit
exit
```
```bash
amir@amir-ubuntu:~$ curl http://localhost:9898
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