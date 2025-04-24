import requests
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    query_clean = animal_name.strip().lower()
    API_KEY = os.getenv('API_KEY')
    API_URL = f"https://api.api-ninjas.com/v1/animals?name={query_clean}"

    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
