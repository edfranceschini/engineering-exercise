FROM python:3.10

WORKDIR /usr/app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt

EXPOSE 8000

ENV APP_MODULE=app.wsgi:app

ENTRYPOINT [ "./entrypoint.sh" ]