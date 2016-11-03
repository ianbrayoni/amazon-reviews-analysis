FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/app
WORKDIR /opt/app
COPY ./requirements /tmp
RUN pip install -r /tmp/development.txt
ADD . /opt/app

CMD ./wait-for-it.sh db:5432 \
    && python manage.py migrate \
    && python manage.py runserver 0.0.0.0:3000
