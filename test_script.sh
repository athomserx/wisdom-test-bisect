#!/bin/bash

# Este archibo puede ser por ejemplo algo que verifique si el projecto corre como `npm build` o `uvicorn app.main:app`

python3 main.py

if [ $? -eq 0 ]; then
  echo "Test passed, this commit is good"
  exit 0
else
  echo "Exception found or test failed: This commit is BAD"
  exit 1
fi