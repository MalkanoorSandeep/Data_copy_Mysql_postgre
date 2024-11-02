from mysql_connection import get_mysql_db_connection
from postgre_connection import get_postgresql_db_connection
from sqlalchemy import *
from loguru import logger
from table_list import listing_tables
import os
        

if __name__ == "__main__":

    server = input("Enter the server which you want to connect 'mysql' server/'postgresql' server: ").lower()

    if server == 'mysql':
        engine = get_mysql_db_connection()
        logger.info(f"Connected successfully to MySQL server on host: {engine.url.host}")
        with engine.connect() as connected:
            logger.info(f"connected successfully to the {server} sever and database {os.getenv('MYSQL_DATABASE')}")

    elif server == 'postgre':
        engine = get_postgresql_db_connection()
        logger.info(f"Connected successfully to MySQL server on host: {engine.url.host}")
        with engine.connect() as connected:
            logger.info(f"connected successfully to the {server} sever and database {os.getenv('POSTGRESQL_DATABASE')}")
    
    else:
        logger.info("Invalid server name please enter the valid server name which mysql or postgresql")
    

    tables = listing_tables(engine)
    # record_count(tables)
