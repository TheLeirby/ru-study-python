import re
from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rating(movie: dict) -> float:
            return float(movie["rating_kinopoisk"]) if len(movie["country"].split(",")) >= 2 else 0

        def get_rating_medium(rating_list: list) -> float:
            rating_sum, rating_num = 0, 0
            for i in rating_list:
                rating_sum, rating_num = rating_sum + i, rating_num + 1
            return rating_sum / rating_num

        return get_rating_medium(list(map(get_rating, list_of_movies)))

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def get_name_rait(movie: dict) -> str:
            if movie["rating_kinopoisk"] >= rating:
                return movie["name"]
            return ""

        return len(re.findall("и", "".join(map(get_name_rait, list_of_movies))))
