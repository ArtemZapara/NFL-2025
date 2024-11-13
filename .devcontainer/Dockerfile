FROM python:3.13-slim

RUN apt-get update && apt-get install -y unzip

WORKDIR /nfl
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV KAGGLE_CONFIG_DIR=/.kaggle
ENV COMPETITION_NAME=nfl-big-data-bowl-2025
ENV DOWNLOAD_PATH=/nfl/data
ENV EXTRACT_PATH=${DOWNLOAD_PATH}/${COMPETITION_NAME}

COPY /secrets/kaggle.json ${KAGGLE_CONFIG_DIR}/kaggle.json
RUN chmod 600 ${KAGGLE_CONFIG_DIR}/kaggle.json

COPY src/ src/
RUN bash src/download.sh