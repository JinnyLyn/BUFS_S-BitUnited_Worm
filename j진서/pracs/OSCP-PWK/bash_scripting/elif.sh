#/bin/bash

read -p "What's your age: " age
if [ $age -lt 16 ]; then
  echo "You might need parental permission to take this course!"
elif [ $age -gt 60 ]; then
  echo "Hats off to you, respect!"
else
  echo "Welcome to the course!"
fi
