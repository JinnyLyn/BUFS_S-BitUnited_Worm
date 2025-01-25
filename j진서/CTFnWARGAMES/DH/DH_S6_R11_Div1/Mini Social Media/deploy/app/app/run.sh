#!/bin/sh

export MYSQL_USER=dbuser
export MYSQL_PASSWORD=dbpass

sleep 5

while true; do flask run -h 0.0.0.0 ; done