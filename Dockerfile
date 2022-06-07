FROM voorloop/decouphage:latest
ENV TZ=Europe/Copenhagen
ENV DEBIAN_FRONTEND=noninteractive

CMD python pipeline.py