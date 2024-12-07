#!/bin/bash
# cSpell: words Kaggle

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


if [[ ! -d "$FONT_DIR" ]]; then
    echo "Creating font directory at $FONT_DIR..."
    mkdir -p "$FONT_DIR"
fi

if [[ ! -f "$FONT_DIR/$FONT_NAME" ]]; then
    echo "Downloading font from $FONT_URL..."
    curl -sSfL "$FONT_URL" -o "$FONT_DIR/$FONT_NAME"
else
    echo "Font $FONT_NAME already exists in $FONT_DIR. Skipping download."
fi
