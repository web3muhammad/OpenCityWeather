class _WeatherLogging:

    def __init__(self, city: str, weather: str, time: str) -> None:
        """Передаем информацию о городе"""
        self.city = city
        self.weather = weather
        self.time = time

    def __print_in_terminal(self) -> None:
        """Записываем результат в терминал"""
        print(f'{self.city}_{self.time}_{self.weather}')

    def __print_in_log(self) -> None:
        """Записываем результат в лог"""
        with open('result.log', 'w', encoding='UTF-8') as file:
            file.write(f'{self.city}_{self.time}_{self.weather}')

    def execute(self) -> None:
        """Выполняем методы выше"""
        self.__print_in_terminal()
        self.__print_in_log()