from db_connection import get_db_connection
from loguru import logger
import pandas as pd
import os

def listing_tables():
     if connection:
            cursor = connection.cursor()
            cursor.execute("show tables")
            table_list = cursor.fetchall()
            logger.info(f"Total tables found: {len(table_list)}")
            table_names = [table[0] for table in table_list]
            logger.info(f"Tables are: {table_names}")
            return table_names

def record_count(tables):
     cursor = connection.cursor()
     logger.info(f"The number of records present in each table:")
     for table in tables:
        query = f"SELECT COUNT(*) FROM `{table}`"
        cursor.execute(query)
        output = cursor.fetchone()
        logger.info(f"{table} : {output[0]}")
        

if __name__ == "__main__":
    connection = get_db_connection()
    tables = listing_tables()
    record_count(tables)
