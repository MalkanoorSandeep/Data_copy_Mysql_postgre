import os
from dotenv import load_dotenv
from mysql.connector import DatabaseError, Error
from loguru import logger
import getpass


db_env = os.getenv("environment", "dev")
load_dotenv(f"/Users/sandeepmalkanoor/Documents/Python/Project1/.env.{db_env}")

if db_env == 'dev': 

    def mysql_config():
        MYSQL_CONFIG = {
            'host': os.getenv('MYSQL_HOST'),                             # MySQL server host
            'user': input("Enter MySQL username: "),                     # MySQL username
            'password': getpass.getpass("Enter MySQL password: "),       # MySQL password
            'database': input("Enter database name: ")     
        }

        os.environ['MYSQL_DATABASE'] = MYSQL_CONFIG['database']
        os.environ['MYSQL_USERNAME'] = MYSQL_CONFIG['user']
        os.environ['MYSQL_PASSWORD'] = MYSQL_CONFIG['password']

        return MYSQL_CONFIG


    def postgresql_config():
        POSTGRESQL_CONFIG = {
            'host' : os.getenv('POSTGRESQL_HOST'),
            'user' : input("Enter Postgre username: "),
            'password' : getpass.getpass("Enter Postgre password: "),
            'database' : input("Enter the database name: "),
            'port' : os.getenv('POSTGRESQL_PORT')
        }
        os.environ['POSTGRESQL_DATABASE'] = POSTGRESQL_CONFIG['database']
        os.environ['POSTGRESQL_USERNAME'] = POSTGRESQL_CONFIG['user']
        os.environ['POSTGRESQL_PASSWORD'] = POSTGRESQL_CONFIG['password']

        return POSTGRESQL_CONFIG


else:
         
     def mysql_config():

        MYSQL_CONFIG = {
            'host': os.getenv('MYSQL_HOST'),         # MySQL server host
            'user': os.getenv("MYSQL_USERNAME"),     # MySQL username
            'password': os.getenv("MYSQL_PASSWORD"), # MySQL password
            'database': os.getenv("MYSQL_DATABASE")  # MySQL database name
        }

        return MYSQL_CONFIG


     def postgresql_config():
         
        POSTGRESQL_CONFIG = {
            'host' : os.getenv('POSTGRESQL_HOST'),
            'user' : os.getenv("POSTGRESQL_USERNAME"),
            'password' : os.getenv("POSTGRESQL_PASSWORD"),
            'database' : input("POSTGRESQL_DATABASE"),
            'port' : os.getenv('POSTGRESQL_PORT')
        }

        return POSTGRESQL_CONFIG

