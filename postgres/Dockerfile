FROM postgres:alpine

COPY ./backup /docker-entrypoint-initdb.d

CMD ["docker-entrypoint.sh", "postgres"]
