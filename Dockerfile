FROM python:3

MAINTAINER daemonchild

COPY app/ /app/
ADD requirements.txt /app/

RUN pip install -r /app/requirements.txt

EXPOSE 9000

CMD [ "python", "/app/file-generator-api.py" ]