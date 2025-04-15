import pandas as pd
import requests
import time

# Carica il file CSV con tab come separatore
file_path = '/Users/riccardosaporiti/Documents/Dataset Wired/IVG_arricchito.csv'
df = pd.read_csv(file_path, sep='\t', encoding='utf-8')

# Imposta la tua API key di HERE Maps
api_key = 'VLyFkWDERonC4CBwzHN-etuW3bct2sSsbgGv-5E3LAk'

# Funzione per geocodificare un singolo indirizzo
def geocode_address(address):
    url = "https://geocode.search.hereapi.com/v1/geocode"
    params = {
        'q': address,
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            position = data['items'][0]['position']
            return position['lat'], position['lng']
    return None, None

# Applica la geocodifica a ogni riga
latitudes = []
longitudes = []

for i, row in df.iterrows():
    address = f"{row['Indirizzo']}, {row['Comune']}, {row['Provincia']}, Italia"
    lat, lng = geocode_address(address)
    latitudes.append(lat)
    longitudes.append(lng)
    time.sleep(1)  # per evitare di superare il rate limit dell'API

# Aggiunge le colonne al DataFrame
df['Latitudine'] = latitudes
df['Longitudine'] = longitudes

# Salva il risultato
output_path = '/Users/riccardosaporiti/Documents/Dataset Wired/IGV_geocoded.csv'
df.to_csv(output_path, index=False)

print(f"File salvato in: {output_path}")