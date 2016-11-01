FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/app
WORKDIR /opt/app
COPY ./requirements /tmp
RUN pip install -r /tmp/development.txt
ADD . /opt/app

CMD ["/bin/bash", "./devops/run.sh"]