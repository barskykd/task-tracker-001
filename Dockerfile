FROM ghcr.io/astral-sh/uv:alpine3.23
ENV PYTHONDONTWRITEBYTECODE=1
ADD --link pyproject.toml uv.lock /app/
WORKDIR /app/

RUN ["uv", "sync"]
ADD --link ./ /app/
RUN chmod +x docker-entrypoint.sh
RUN mkdir /data

ENV TASK_TRACKER_SQLITE_FILE=/data/db.sqlite3                        
ENV TASK_TRACKER_STATIC_ROOT=/static_root/
ENV TASK_TRACKER_DEBUG=0
ENV TASK_TRACKER_SECRET_KEY_FILE=/data/secretkey
ENV TASK_TRACKER_ALLOWED_HOSTS=127.0.0.1,localhost
RUN ["uv", "run", "manage.py", "collectstatic"]

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD [ "runserver" ]
