from os import getenv

SECRET_KEY = getenv('SECRET')
DB_HOST = getenv("HOST")
DB_USER = getenv("USER")
DB_PASSWORD = getenv("PASSWORD")
DB_DATABASE = getenv("NAME")

CLOUD_NAME = getenv('CLOUD_NAME')
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')