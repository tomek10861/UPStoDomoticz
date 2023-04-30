FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    nut-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install requests

COPY UPStoDomoticz.py .

CMD ["python", "UPStoDomoticz.py"]
