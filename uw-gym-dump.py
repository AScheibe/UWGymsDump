import os
import requests
import pandas as pd
import json
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('API_URL')

response = requests.get(url)

json_str = response.content

if isinstance(json_str, bytes):
    json_str = json_str.decode('utf-8')

data = json.loads(json_str)

df = pd.DataFrame(data)

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT'))
name = os.getenv('NAME')

engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{name}', echo=False)

df.to_sql(name='uwgyms', con=engine, if_exists='append', index=False)