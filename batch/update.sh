#!/usr/bin/env bash

PROJECT_PATH="/project/gwparser"

cd $PROJECT_PATH

docker-compose -f $PROJECT_PATH/docker/docker-compose.yml build

docker-compose -f $PROJECT_PATH/docker/docker-compose.yml rm -f -s

docker-compose -f $PROJECT_PATH/docker/docker-compose.yml up -d