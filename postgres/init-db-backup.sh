#!/bin/sh
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -h db -p 5432 -U $POSTGRES_USER $POSTGRES_DB < gutendex.dump
