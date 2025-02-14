#!/bin/bash

#prompt for user credentials

read -p 'Username : ' username
read -sp 'Password : ' password

echo "Thanks! Your creds are as follows: " $username " and " $password
