Flask Docker
==============

Simple API
--------------

# Requirements
* [Docker](https://docs.docker.com/engine/installation/)

# Build image
``` bash
$ docker build -t gloriapg/flask-docker  .
```
# Docker RUN

``` bash
$ docker run --name flask-docker  -d -p 8000:8000 gloriapg/flask-docker
$ docker exec -it flask-docker service supervisor start
```

