FROM python:3.7.3-alpine3.9
RUN set -ex; \
    apk add --no-cache --virtual .buildDeps gcc libcouchbase-dev; \
    apk add --no-cache libcouchbase libffi-dev libxml2-dev libxslt-dev;
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "webservice.py" ]