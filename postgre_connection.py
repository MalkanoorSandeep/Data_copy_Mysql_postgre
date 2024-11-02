# engine = create_engine(
#     f"postgresql+pg8000://{username}:{password}@{host}:{port}/{database}",
#     connect_args={"timeout": 10}

from config import postgresql_config
from sqlalchemy import create_engine
from loguru import logger
import urllib.parse

def get_postgresql_db_connection():
    try:

        POSTGRESQL_CONFIG=postgresql_config()

        host = POSTGRESQL_CONFIG['host']
        username = POSTGRESQL_CONFIG['user']
        password = urllib.parse.quote_plus(POSTGRESQL_CONFIG['password'])
        database = POSTGRESQL_CONFIG['database']
        port = POSTGRESQL_CONFIG['port']

        engine = create_engine(
            f"postgresql+pg8000://{username}:{password}@{host}:{port}/{database}",
            connect_args={"timeout": 10}
        )

        return engine

      


    except Exception as e:
        logger.error(f"Error connecting to PostgreSQL: {e}")
        return None