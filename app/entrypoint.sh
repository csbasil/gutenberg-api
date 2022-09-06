#!/bin/sh
if [[ "$DEBUG" = "True" ]]; then
    uvicorn --reload --host 0.0.0.0 --port ${PORT:-8000} main:app
else
    uvicorn --host 0.0.0.0 --port ${PORT:-8000} main:app
fi
