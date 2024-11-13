FROM python:3.13-slim

WORKDIR /nfl
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV KAGGLE_CONFIG_DIR=/.kaggle
COPY /secrets/kaggle.json ${KAGGLE_CONFIG_DIR}/kaggle.json
RUN chmod 600 ${KAGGLE_CONFIG_DIR}/kaggle.json