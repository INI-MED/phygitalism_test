FROM python:3.8-slim-buster
WORKDIR /test
RUN python3 -m venv venv

COPY requirements.txt .
RUN . ./venv/bin/activate && pip install -r requirements.txt

ADD . .
EXPOSE 5000
CMD . ./venv/bin/activate && exec python app.py
