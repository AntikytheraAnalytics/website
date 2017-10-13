FROM python:3.6-alpine

RUN pip install gunicorn

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY app.py /app/
COPY templates /app/templates

EXPOSE 8000
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":8000", "-w", "4", "app:app"]
