#!/bin/bash

ZIP_FILE="${DOWNLOAD_PATH}/${COMPETITION_NAME}.zip"
EXTRACT_DIR="${EXTRACT_PATH}"

if [ ! -f "${KAGGLE_CONFIG_DIR}/kaggle.json" ]; then
    echo "Error: Kaggle credentials not found at ${KAGGLE_CONFIG_DIR}/kaggle.json"
    exit 1
fi

if [ -f "${ZIP_FILE}" ]; then
    echo "Data already downloaded at ${ZIP_FILE}."
else
    echo "Downloading competition data..."
    kaggle competitions download ${COMPETITION_NAME} -p ${DOWNLOAD_PATH}
fi

if [ -d "${EXTRACT_DIR}" ] && [ "$(ls -A ${EXTRACT_DIR})" ]; then
    echo "Data already extracted at ${EXTRACT_DIR}."
else
    echo "Extracting competition data..."
    unzip -o ${ZIP_FILE} -d ${EXTRACT_DIR}
fi