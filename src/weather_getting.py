import httpx
import datetime as dt


class _WeatherGetting:

    @staticmethod
    def __get_city_coordinates(api_key: str, city: str) -> tuple:
        """Получаем координаты города по API"""
        city_data = httpx.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}').json()[0]
        return city_data["lat"], city_data["lon"]

    @staticmethod
    def __get_city_data(api_key: str, lat: str, lon: str) -> tuple:
        """Получаем информацию о погоде, текущее время и временную зону по координатам"""
        city_data = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&appid={api_key}').json()
        return city_data['weather'][0]['description'], city_data['dt'], city_data['timezone']

    @staticmethod
    def __format_city_time(city_timestamp: int, city_timezone: int) -> str:
        """Форматируем текущее время под временную зону города"""
        formatted_timezone = dt.timezone(dt.timedelta(seconds=city_timezone))
        formatted_time = dt.datetime.fromtimestamp(city_timestamp, formatted_timezone).strftime('%Y-%m-%d_%H:%M')
        return formatted_time

    def execute(self, api_key: str, city: str) -> tuple:
        """Получаем информацию о погоде и отформатированное время"""
        lat, lon = self.__get_city_coordinates(api_key, city)
        weather, timestamp, timezone = self.__get_city_data(api_key, lat, lon)
        time = self.__format_city_time(timestamp, timezone)
        return weather, time

