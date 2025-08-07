#!/bin/bash

# Activate virtual environment if it exists
if [ -d "env" ]; then
    source env/bin/activate
fi

# Start the server
uvicorn app.main:app --host 0.0.0.0 --port 9174 --reload 