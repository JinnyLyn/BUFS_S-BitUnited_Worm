FROM python:3.11-alpine

ENV USER chall
ENV PORT 5000

RUN apk add curl

# Add user
RUN adduser -D -g "" $USER

# Add files
COPY --chown=root:root app /app

WORKDIR /app
RUN chmod 705 run.sh
RUN chmod 777 tmp
RUN pip install -r requirements.txt

USER $USER
EXPOSE $PORT

ENTRYPOINT ["/bin/ash"]
CMD ["./run.sh"]
