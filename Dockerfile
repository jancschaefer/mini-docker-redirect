FROM python:3.10-slim-bullseye AS compile

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.10-slim-bullseye AS build
COPY --from=compile /root/.local /root/.local

COPY app /app
WORKDIR /app

EXPOSE 5000

ENV PATH=/root/.local/bin:$PATH
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]%