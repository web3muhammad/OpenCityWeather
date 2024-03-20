from src.weather_getting import _WeatherGetting
from src.weather_logging import _WeatherLogging


class OpenCityWeather:

    def __init__(self) -> None:
        """Передаем классы"""
        self.__weather_getting = _WeatherGetting
        self.__weather_logging = _WeatherLogging

    def __get_data(self, api_key: str, city: str) -> tuple:
        """Инициализируем работу запросов и возвращаем погоду и время"""
        return self.__weather_getting().execute(api_key, city)

    def __log_data(self, city: str, weather: str, time: str) -> None:
        """Передаем погоду и время для дальнейшей записи"""
        self.__weather_logging(city, weather, time).execute()

    def execute(self, api_key: str, city: str) -> None:
        """Выполняем методы выше"""
        weather, time = self.__get_data(api_key, city)
        self.__log_data(city, weather, time)