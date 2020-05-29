FROM balenalib/raspberry-pi-debian-python:3.7 as base

FROM base AS builder

RUN mkdir /install
WORKDIR /install

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt-get update && apt-get -y install build-essential

COPY src/requirements.txt /tmp/

RUN pip install --install-option="--prefix=/install" -r /tmp/requirements.txt


FROM base

COPY --from=builder /install /usr/local

COPY src/ /app
WORKDIR /app

CMD ["python", "RelayTempTest.py"]
