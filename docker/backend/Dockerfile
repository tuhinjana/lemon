FROM python:3.9-alpine

RUN apk update && apk add --no-cache --virtual bash gcc musl-dev \
    linux-headers jpeg-dev zlib-dev mariadb-dev libffi-dev

RUN rm -rf /usr/bin/mysql* && mkdir -p /apps/
WORKDIR /apps/

# install pypi packages
COPY ./requirements.txt ./requirements.txt
RUN python3.9 -m venv venv && source venv/bin/activate
RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY ./lemon_markets/ /apps/
COPY ./docker/backend/entrypoint.sh /apps/
EXPOSE 8000
CMD ["sh", "./entrypoint.sh"]
#CMD ["tail", "-f", "/dev/null"]