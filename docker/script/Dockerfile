FROM python:3.12-alpine AS builder
COPY app /builds/app
RUN python -m compileall /builds/app

FROM python:3.12-alpine AS runtime
RUN addgroup -g 1998 pc && adduser -D -s /bin/sh -u 1998 -G pc pc
RUN mkdir -p /builds/app && chown pc:pc /builds/app

COPY --from=builder --chown=pc:pc /builds/app /builds/app

RUN rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

USER pc
WORKDIR /builds/app
ENTRYPOINT ["python", "hello.py"]