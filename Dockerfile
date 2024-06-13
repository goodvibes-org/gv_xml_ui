FROM python:3.9-slim

WORKDIR /app
RUN mkdir -p ./data/db_files
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
COPY container.env .env
RUN mkdir -p ./data/db_files/export/dumpy
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]