```bash
docker run -d --name apache -v $(pwd)$:/usr/local/apache2/htdocs  httpd
```
3e13ba53189f9ab0d8e244f00ff4c40511f6947dd9f1cc027f7e3a6c879acafc
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
docker run -d --name apache -v $(pwd):/usr/local/apache2/htdocs -p 9898:80 httpd
```
3e13ba53189f9ab0d8e244f00ff4c40511f6947dd9f1cc027f7e3a6c879acafc
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