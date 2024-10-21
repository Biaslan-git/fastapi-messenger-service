from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.environ.get('DB_HOST')
DB_PORT=os.environ.get('DB_PORT')
DB_NAME=os.environ.get('DB_NAME')
DB_USER=os.environ.get('DB_USER')
DB_PASS=os.environ.get('DB_PASS')
SECRET_KEY=os.environ.get('SECRET_KEY')

if __name__=="__main__":
    print(f'{DB_HOST=}')
    print(f'{DB_PORT=}')
    print(f'{DB_NAME=}')
    print(f'{DB_USER=}')
    print(f'{DB_PASS=}')
    print(f'{SECRET_KEY=}')
