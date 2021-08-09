FROM python:3.8-alpine

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# TODO: Ignore db.sqlite3
COPY ./sharky .
RUN python manage.py migrate

ENTRYPOINT [ "python", "/app/manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]
EXPOSE 8000
