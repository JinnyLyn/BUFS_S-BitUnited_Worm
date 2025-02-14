#!/bin/bash

read -p "What's your age: " age

if [[ $age -lt 16 ]]; then
  echo "You might need parental permissio to take this course!"
else
  echo "Welcome to the course!"
fi
