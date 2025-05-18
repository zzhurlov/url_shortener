from dotenv import load_dotenv

import os

load_dotenv()


DB_URL = os.getenv("DB_URL")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

BYTES_QUANTITY = 16

HOME_PAGE = "http://127.0.0.1:8000/"
