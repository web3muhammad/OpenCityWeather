from src.weather_interface import OpenCityWeather


def main(city: str, api_key: str) -> None:
    """Инициализируем запуск"""
    OpenCityWeather().execute(api_key, city)


if __name__ == '__main__':
    """Спрашиваем API ключ и город, а далее передаем их"""
    client_api_key = input("Введите API ключ: ")
    requested_city = input("Введите город: ")
    main(requested_city, client_api_key)
