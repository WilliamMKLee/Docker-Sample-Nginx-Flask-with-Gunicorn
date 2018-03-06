# Docker Sample: Nginx + Flask with Gunicorn

using dockerswarm to easy scale

nginx as http server
Gunicorn as WSGI server


WSGI request
    nginx ==(http protocol)==> Gunicorn ==(WSGI)==> flask app

HTTP request(static)
    nginx

## Build

```
$ docker-compose build
```

## Run

```
$docker-compose run -d
```

now you can access localhost:80 page to see sample

## Scale

we can scale app part

```
$docker-compose scale web=5
```




