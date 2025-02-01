#!/bin/sh
docker exec -it kickstarter sh -c "./manage.py spectacular --color --file=/exchange/openapi.yaml"
