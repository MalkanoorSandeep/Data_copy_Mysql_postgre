import os
from dotenv import load_dotenv
from mysql.connector import DatabaseError, Error
from loguru import logger
import getpass


db_env = os.getenv("environment", "dev")
load_dotenv(f"/Users/sandeepmalkanoor/Documents/Python/Project1/.env.{db_env}")
   #/Users/sandeepmalkanoor/Documents/Python/Project1/.env.dev_dat_lemur

if db_env == 'dev': 
    MYSQL_CONFIG = {
        'host': os.getenv('MYSQL_HOST'),                             # MySQL server host
        'user': input("Enter MySQL username: "),                     # MySQL username
        'password': getpass.getpass("Enter MySQL password: "),       # MySQL password
        'database': input("Enter database name: ")                   # MySQL database name
    }

else:
    MYSQL_CONFIG = {
        'host': os.getenv('MYSQL_HOST'),         # MySQL server host
        'user': os.getenv("MYSQL_USERNAME"),     # MySQL username
        'password': os.getenv("MYSQL_PASSWORD"), # MySQL password
        'database': os.getenv("MYSQL_DATABASE")  # MySQL database name
    }



