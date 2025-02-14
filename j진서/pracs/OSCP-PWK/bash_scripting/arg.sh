#!/bin/bash

if [[ !$1 || !$2 ]]; then
  echo "You must provide two arguments!!"
  exit 1
fi

echo "The first two arguments are $1 and $2"
