import requests


API_KEY = "58f57049de1f030d55c37dc16469e379"


def get_data(place, forecast_date):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&APPID={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_value = 8 * forecast_date
    filtered_data = filtered_data[:nr_value]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Jhenaidah',forecast_date=5))