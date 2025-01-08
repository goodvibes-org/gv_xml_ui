FROM python:3.9-slim

WORKDIR /app
RUN mkdir -p ./data/db_files
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
COPY container.env .env
# RUN mkdir -p ./data/db_files/export/dumpy
ADD https://api.github.com/repos/goodvibes-org/e2csv-bin/releases/latest metadata
RUN wget https://github.com/goodvibes-org/e2csv-bin/releases/latest/download/excel-to-csv
RUN chmod +x "excel-to-csv"
EXPOSE 9000

HEALTHCHECK CMD curl --fail http://localhost:9000/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=9000", "--server.address=0.0.0.0"]
