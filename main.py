from db_connection import get_db_connection
from loguru import logger
import pandas as pd
import os

def my_sql_conncetion_logic():
     connection = get_db_connection()
     if connection:
            cursor = connection.cursor()
            cursor.execute("show tables")
            table_list = cursor.fetchall()
            logger.info(f"Total tables found: {len(table_list)}")
            logger.info(f"Tables {[table[0] for table in table_list]}")


if __name__ == "__main__":
    my_sql_conncetion_logic()
    