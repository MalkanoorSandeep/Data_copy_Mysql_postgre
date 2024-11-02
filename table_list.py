from sqlalchemy import *
from loguru import logger


def listing_tables(engine):
    try:
        with engine.connect() as connection:
            query = input("Enter the query to retrieve tables in databse: ")
            result = connection.execute(query)
            table_names = [row[0] for row in result]
            logger.info(f"Total tables found: {len(table_names)}")
            logger.info(f"Tables are: {table_names}")
            return table_names
        
    except Exception as e:
        logger.error(f"Error listing tables: {e}")
        return []