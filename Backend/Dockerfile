FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN apt-get update -y  ; apt-get install -y iputils-ping 

RUN pip install -r requirements.txt

EXPOSE 5001

ENV NAME World

CMD ["python", "app.py"]
