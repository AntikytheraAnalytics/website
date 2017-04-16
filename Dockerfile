FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential nodejs npm git
RUN ln -s /usr/bin/nodejs /usr/bin/node
COPY . /app
WORKDIR /app

RUN npm install -g grunt-cli
WORKDIR /app/static/bootstrap-3.3.7/
RUN npm install; exit 0
RUN grunt dist

WORKDIR /app/static
RUN rm -rf typed.js
RUN git clone https://github.com/mattboldt/typed.js.git

WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
