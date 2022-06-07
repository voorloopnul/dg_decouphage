FROM voorloop/decouphage:latest
ENV TZ=Europe/Copenhagen
ENV DEBIAN_FRONTEND=noninteractive

COPY pipeline.py /data/pipeline.py

CMD python /data/pipeline.py