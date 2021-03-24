FROM python:alpine
RUN apk update && \
    apk upgrade && \
    apk add bash && \
    apk add --no-cache --virtual build-deps build-base gcc && \
    pip install aws-sam-cli && \
    apk del build-deps && \
    apk add docker && \
    # apk add openrc --no-cache && \
    apk add sudo
RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
# RUN rc-update add docker boot
RUN rm -rf ./docker
RUN docker logout
# RUN sudo addgroup docker
# RUN sudo addgroup $USER docker
# RUN docker logout
RUN docker start
RUN docker status
RUN sam local start-api -p 8080

# set -o errexit \
#     BASEDIR="$1" \
#     /usr/local/bin/sam local start-lambda \
#     --template dist/template.yaml \
#     --host 0.0.0.0 \
#     --docker-volume-basedir "${BASEDIR}" \
#     --docker-network monsoon-samples_default \
#     --skip-pull-image