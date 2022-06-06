FROM python:3.10.4

WORKDIR /usr/src

COPY / .

EXPOSE 77

ENTRYPOINT [ "python3","Project/src/main.py" ]