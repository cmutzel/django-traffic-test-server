django-docker
=============

This project launches a simple django app within a docker container

Build the image...
$> docker build -t traffic-app .

Run the app
$> docker run --name traffic-app-1 -p 8000:8000 -d  traffic-app

if using boot2docker, get the ip we need to hit:
$> boot2docker ip