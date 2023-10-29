FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y gdal-bin libgdal-dev

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app/src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]