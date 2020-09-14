# Pizza-identification
An artificial intelligence application to identify pizza. Using flutter, python, and tensorflow. 

Steps
--------
Build Docker Image according to Dockerfile named "ai-pizza"
```
docker build -t ai-pizza .
```

Create docker container with the image you just created
```
docker run --name ai-pizza -dp 5000:5000 ai-pizza
```

CURL to check it works
```
curl localhost:5000
```

Enjoy using <b>Postman</b> to test
```
POST to /upload
form-data:
  key: file
  value: your file <Click and select it>
```

GOOD LUCK
