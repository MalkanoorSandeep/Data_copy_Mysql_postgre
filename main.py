import mysql.connector
from mysql.connector import InterfaceError, DatabaseError, ProgrammingError, Error
from config import MYSQL_CONFIG
from loguru import logger
import pandas as pd
import os

def my_sql_conncetion():
    try:
        connection = mysql.connector.connect(
            host = MYSQL_CONFIG['host_name'],
            user = MYSQL_CONFIG['user_name'],
            password = MYSQL_CONFIG['password'],
            database = MYSQL_CONFIG['database']
        )

        if connection.is_connected():
            logger.info("Successfully connected to MySQL")
            cursor = connection.cursor()
            cursor.execute("select * from `technology_skills_15-1252-00`;")
            column_names = [col[0] for col in cursor.description]
            records = cursor.fetchall()
            # print(f"Connected to the database: {record}")
            
            # logger.info(f"{columns}")
            df = pd.DataFrame(records, columns = column_names)
            logger.info(f"{df.head(2)}")
            # print(df.head(2))

    except InterfaceError as e:
        logger.error(f"Database connection error: {e}")

    except DatabaseError as e:
        logger.error(f"General database error: {e}")

    except ProgrammingError as e:
        logger.error(f"SQL syntax or programming error: {e}")

    except Error as e:
        logger.error(f"Other MySQL-related error: {e}")

    except Exception as e:
        logger.error(f"General error in code logic: {e}")


# info=os.stat('/Users/sandeepmalkanoor/Documents/Python/Project1/config.py')
# print(f'{info.st_mtime}')
# print(f'{info.st_size}')

if __name__ == "__main__":
    my_sql_conncetion()
    