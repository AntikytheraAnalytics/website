FROM gliderlabs/alpine:3.3

RUN apk add --update python py-pip

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt


COPY app.py /app/
COPY static/images /app/static/images
COPY templates /app/templates
COPY static/bootstrap-4.0.0-beta/dist/css/bootstrap.min.css /app/static/bootstrap-4.0.0-beta/dist/css/

ENTRYPOINT ["python"]
CMD ["app.py"]
