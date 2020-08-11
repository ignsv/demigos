FROM python:3.6.5

RUN apt update \
    # GDAL
    && apt install gdal-bin -y \
    # PostgreSQL dependencies
    && apt install -y libpq-dev postgresql-client-9.6

WORKDIR /app
COPY requirements/ requirements/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
