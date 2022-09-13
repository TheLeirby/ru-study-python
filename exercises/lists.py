class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if len(input_list) == 0:
            return input_list
        maximum_value, replace_list = max(input_list), []
        for i in input_list:
            replace_list.append((i, maximum_value)[i > 0])
        return replace_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        i = 0
        while i <= len(input_list):
            if input_list[i] == query:
                return i
            i += 1
        return -1
