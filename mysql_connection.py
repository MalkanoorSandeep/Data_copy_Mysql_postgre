from sqlalchemy import create_engine
from config import mysql_config
from loguru import logger
import urllib.parse

def get_mysql_db_connection():
     try:

        MYSQL_CONFIG = mysql_config()

        host = MYSQL_CONFIG['host'] 
        username = MYSQL_CONFIG['user'] 
        password = urllib.parse.quote_plus(MYSQL_CONFIG['password'])
        database = MYSQL_CONFIG['database']


        # Debugging logs to verify values
        # logger.debug(f"Host: {host}")
        # logger.debug(f"Username: {username}")
        # logger.debug(f"Database: {database}")
        # logger.debug(f"Database: {password}")


        engine = create_engine(
             f"mysql+pymysql://{username}:{password}@{host}/{database}"
        )

        return engine


     except Exception as e:
        logger.error(f"Database conncetion error: {e}")
        return None


# if __name__ == "__main__":
#     engine = get_mysql_db_connection()
#     if engine:
#         logger.info("Engine created successfully.")
#     else:
#         logger.error("Failed to create engine.")