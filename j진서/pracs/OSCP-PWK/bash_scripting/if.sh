#!/bin/bash

read -p "What is your age: " age

if [[ $age -lt 16 ]]; then
  echo "You might need parental permission to take this course!"
fi
