FROM voorloop/decouphage:latest
ENV TZ=Europe/Copenhagen
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt -y install wget && \
    rm -rf /var/lib/apt/lists/* && apt clean

COPY pipeline.py /data/pipeline.py

CMD python /data/pipeline.py