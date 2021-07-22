FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

# Pacotes que eu necessito instalar
RUN apt-get update && apt-get install -y \
	libopencv-dev \
        python3-pip \
	python3-opencv && \
    rm -rf /var/lib/apt/lists/*

# Bibliotecas python
RUN pip3 install tensorflow && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py && \
    pip3 install keras --no-deps && \
    pip3 install opencv-python && \
    pip3 install imutils && \
    pip3 install bokeh

RUN pip3 install pybase64 xlrd 

WORKDIR /opt/

COPY templates /opt/templates

VOLUME ["/opt/data"]

COPY modelo.json /opt/modelo.json
COPY modelo.h5 /opt/modelo.h5
COPY medias.csv /opt/mean.csv
COPY variancias.csv /opt/var.csv
COPY CnnClass.py /opt/CnnClass.py
COPY principal.py /opt/principal.py
COPY exec.sh /opt/exec.sh

EXPOSE 5006

ENTRYPOINT  [ "bash", "/opt/exec.sh" ]