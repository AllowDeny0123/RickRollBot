from alpine:latest

#Updating repositories list by adding "community" one
RUN sed -i '2 s/^#//g' /etc/apk/repositories && \
    apk update

RUN apk add ffmpeg python3

WORKDIR /code
COPY assets/1.mp3 ./assets/1.mp3
COPY src/main.py main.py
COPY requirements.txt .
RUN python3 -m venv venv
RUN ./venv/bin/pip install -r requirements.txt

CMD ["./venv/bin/python", "main.py"]
