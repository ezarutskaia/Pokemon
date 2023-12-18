import requests
import pandas as pd
import json
import time
import random
from sqlalchemy import create_engine
from faker import Faker

fake = Faker()
#Faker.seed(0)

engine = create_engine('mysql+pymysql://root:secret@localhost:4306/Pokemon')

headers = {
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
}

pokemon = pd.DataFrame(columns=['pokemon_id', 'name', 'height', 'weight'])
types = pd.DataFrame(columns=['pokemon_id', 'type'])
stats = pd.DataFrame(columns=['pokemon_id', 'stat', 'base_stat'])

i = 1
while i<=1000:
    print('start',i)
    if (i % 103) == 0:
       headers = {
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': fake.chrome()
        } 
    if (i % 2) == 0:
        time.sleep(random.uniform(0.5, 2))
    try:
        with requests.get('https://pokeapi.co/api/v2/pokemon/'+ str(i)+ '/', headers=headers) as url:
            if (len(url.text) < 20):
                raise Exception(url.text)
            data = json.loads(url.text)           
            pokemon.loc[ len(pokemon.index )] = [data['id'], data['name'], data['height'], data['weight']]
            for item in data['types']:
                types.loc[ len(types.index )] = [data['id'], item['type']['name']]
            for item in data['stats']:
                stats.loc[ len(stats.index )] = [data['id'], item['stat']['name'], item['base_stat']]
    except Exception as e:
        print(e)
    i += 1

pokemon.to_sql('pokemon', con=engine, if_exists='append', index=False)
types.to_sql('types', con=engine, if_exists='append', index=False)
stats.to_sql('stats', con=engine, if_exists='append', index=False)
#print(pokemon, types, stats)


