FROM python:3.7.3-strech

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY src/ /app
WORKDIR /app

CMD["python", "RelayTempTest.py"]
