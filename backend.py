import requests


API_KEY = "58f57049de1f030d55c37dc16469e379"


def get_data(place, forecast_date, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&APPID={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_value = 8 * forecast_date
    filtered_data = filtered_data[:nr_value]
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Jhenaidah',forecast_date=5,kind='Sky'))