import pandas as pd
import os
from sqlalchemy import create_engine, text
import logging
import time
import pymysql


# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)


# Logging Setup
logging.basicConfig(
    filename="logs/file_ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


# Create database if not exists
engine_root = create_engine("mysql+pymysql://root:Password1@localhost:3306")

with engine_root.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS inventory_db;"))

# Engine for actual data loading
engine = create_engine("mysql+pymysql://root:Password1@localhost:3306/inventory_db")


# Ingest normal size CSV
def ingest_full(df, table_name):
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    logging.info(f"Loaded full file into table: {table_name}")


# Ingest large CSV in chunks (prevents memory overflow)
def ingest_in_chunks(file_path, table_name, chunksize=200000):
    logging.info(f"Chunked ingestion started for {file_path}...")

    first_chunk = True
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        chunk.to_sql(
            table_name,
            con=engine,
            if_exists="replace" if first_chunk else "append",
            index=False
        )
        first_chunk = False
        logging.info(f"{len(chunk)} rows written to {table_name}...")

    logging.info(f"Chunked ingestion completed for {table_name}")


# Main loader
def load_raw_data():
    start = time.time()

    for file in os.listdir("data"):
        if file.endswith(".csv"):
            file_path = os.path.join("data", file)
            table_name = file[:-4]

            try:
                file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB

                logging.info(f"Processing file: {file} ({file_size:.2f} MB)")

                if file_size > 200:  # threshold for heavy files
                    ingest_in_chunks(file_path, table_name)
                else:
                    df = pd.read_csv(file_path)
                    ingest_full(df, table_name)

            except Exception as e:
                logging.error(f"Failed to ingest {file}: {e}")

    total_time = (time.time() - start) / 60
    logging.info("-------------- Ingestion Complete ------------")
    logging.info(f"Total Time Taken: {total_time:.2f} minutes")


# Run Script
if __name__ == "__main__":
    load_raw_data()