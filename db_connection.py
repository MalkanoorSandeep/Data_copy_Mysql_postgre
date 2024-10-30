import mysql.connector
from mysql.connector import Error, DatabaseError
from config import MYSQL_CONFIG
from loguru import logger


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host = MYSQL_CONFIG['host'], 
            username = MYSQL_CONFIG['user'], 
            password = MYSQL_CONFIG['password'],
            database = MYSQL_CONFIG['database']
        )

        if connection.is_connected():
            logger.info(f"Connected to the database: {MYSQL_CONFIG['database']}")
            return connection
        

    except DatabaseError as e:
        # Specific error handling for an invalid database name
        if e.errno == 1049:  # Error code for "Unknown database"
            logger.error("Invalid database name specified or database not found.")
        else:
            logger.error(f"Database error: {e}")
        return None


    except Error as e:
        logger.error(f"Database conncetion error: {e}")
        return None