FROM python:3.10

RUN apt-get update && \
    apt-get install -y gdal-bin libgdal-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


WORKDIR /app

COPY . /app

EXPOSE 8000

WORKDIR /app/src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]