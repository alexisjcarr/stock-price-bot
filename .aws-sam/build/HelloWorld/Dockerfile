FROM public.ecr.aws/lambda/python:latest
RUN pip install aws-sam-cli
RUN mkdir /app
WORKDIR /app
COPY Pipfile Pipfile
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
RUN pip install decouple
COPY . .
EXPOSE 8080
RUN sam local start-api -p 8080 --docker


