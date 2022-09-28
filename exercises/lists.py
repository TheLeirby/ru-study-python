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

        low = 0
        high = len(input_list) - 1
        search_res = -1
        while low <= high:
            middle = (low + high) // 2
            guess = input_list[middle]
            if guess == query:
                return middle
            if guess > query:
                high = middle - 1
            else:
                low = middle + 1
        return search_res
