import os
from dotenv import load_dotenv
from mysql.connector import DatabaseError, Error
from loguru import logger
import getpass


db_env = os.getenv("environment", "dev")
load_dotenv(f"/Users/sandeepmalkanoor/Documents/Python/Project1/.env.{db_env}")
   #/Users/sandeepmalkanoor/Documents/Python/Project1/.env.dev_dat_lemur

   
MYSQL_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),         # MySQL server host
    'user': os.getenv('MYSQL_USER'),        # MySQL username
    'password': None,                       # MySQL password
    'database': os.getenv('MYSQL_DATABASE')  # MySQL database name
}

# Prompt for username if it's not provided in environment variables
if MYSQL_CONFIG['user'] is None:
    MYSQL_CONFIG['user'] = input("Enter MySQL username: ")

# Always prompt for password at runtime if not set
MYSQL_CONFIG['password'] = getpass.getpass("Enter MySQL password: ")

# Log final MYSQL_CONFIG to check if values were updated
logger.info(f"Connected to the database: {MYSQL_CONFIG['database']}")