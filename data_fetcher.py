import requests


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
    API_KEY = "05tc3hKebxY7ckKz2pP8kA==x8KUa85LA30Jf4xu"
    API_URL = f"https://api.api-ninjas.com/v1/animals?name={query_clean}"

    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
