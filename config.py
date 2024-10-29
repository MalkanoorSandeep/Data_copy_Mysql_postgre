import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
MYSQL_CONFIG = {
    'host_name': os.getenv('MYSQL_HOST'),         # MySQL server host
    'user_name': os.getenv('MYSQL_USER'),     # MySQL username
    'password': os.getenv('MYSQL_PASSWORD'), # MySQL password
    'database': os.getenv('MYSQL_DATABASE')  # MySQL database name
}


