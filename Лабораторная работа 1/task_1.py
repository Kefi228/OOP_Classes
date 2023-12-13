from typing import Union


class Table:
    def __init__(self, height: Union[int | float], width: Union[int | float], length: Union[int | float]):
        """Создание и подготовка к работе объекта "Cтол"

            :param height: высота
            :param width: ширина
            :param length: длина

            Примеры:
            >>> table = Table(1, 2, 3) #инициализация экземпляра класса
        """

        if not isinstance(height, Union[int, float]):
            raise TypeError("Высота должна быть типом int или float")
        if 0 > height:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(width, Union[int | float]):
            raise TypeError("Ширина должна быть типом int или float")
        if 0 > width:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(length, Union[int | float]):
            raise TypeError("Длина должна быть типом int или float")
        if 0 > length:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        self.getHeight()
        self.standUpTable()
        self.setWidth()

    def getHeight(self) -> int:
        """Данный метод возвращает
         высоту стола.

         :return: высота стола

         Примеры:
         >>> table = Table(10, 9, 8)
         >>> table.getHeight()
         """
        ...

    def standUpTable(self) -> None:
        """Данный метод описывает действие:
         поставить стол

         Примеры:
         >>> table = Table(10, 9, 8)
         >>> table.standUpTable()
         """
        ...

    def setWidth(self, width: int) -> None:
        """Данный метод устанавливает
        значение ширины стола

        :param width:новое значение ширины

        Примеры:
        >>> table = Table(10, 9, 8)
        >>> table.setWidth(15)
        """
        ...


class Tree:
    def __init__(self, type_tree: str, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

            :param type_tree: тип дерева
            :param age: возраст

            Примеры:
            >>> tree = Tree("Дуб", 500) #инициализация экземпляра класса
        """
        if not isinstance(type_tree, str):
            raise TypeError("Тип дерева должен быть типом str")
        self.type_tree = type_tree

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типо int")
        if 0 > age:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        self.waterTree()
        self.getAge()
        self.setTypeTree()

    def waterTree(self) -> None:
        """Данный метод описывает действие:
         полить дерево

         Примеры:
         >>> tree = Tree("Дуб", 500)
         >>> tree.waterTree()
         """
        ...

    def getAge(self) -> int:
        """Данный метод возвращает
         возраст дерева

         :return: возраст дерева

         Примеры:
         >>> tree = Tree("Дуб", 500)
         >>> tree.getAge()
         """
        ...

    def setTypeTree(self, type_tree: str) -> None:
        """Данный метод устанавливает
        значение типа дерева

        :param type_tree: тип дерева

        Примеры:
        >>> tree = Tree("Дуб", 500)
        >>> tree.setTypeTree("Клён")
        """
        ...


class Facebook:
    def __init__(self, post: str, count_like: int):
        """ Создание и подготовка к работе объекта "Facebook"

            :param post: пост
            :param count_like: количество лайков

            Примеры:
            >>> post = Facebook("Привет", 10) #инициализация экземпляра класса
            """
        if not isinstance(post, str):
            raise TypeError("Пост должен быть типом str")
        self.post = post

        if not isinstance(count_like, int):
            raise TypeError("Количество лайков должен быть типом int")
        if 0 > count_like:
            raise ValueError("Количество лайков должно быть положительным числом")
        self.count_like = count_like

        self.sendPost()
        self.likePost()

    def sendPost(self):
        """Данный метод описывает действие:
        опубликовать пост

        :return: Готовый пост

        Примеры:
        >>>post = Facebook("Привет", 10)
        >>>post.sendPost()
        """
        ...

    def likePost(self):
        """Данный метод описывает действие:
        оценить пост

        Примеры:
        >>> post = Facebook("Привет", 10)
        >>> post.likePost()
        """
        ...


if __name__ == "__main__":
    table = Table(12, 15, 10)
    tree = Tree("Дуб", 100)
    post = Facebook("Какой хороший день", 25)
    print(table, tree, post)
    help(table)
    help(tree)
    help(post)
    pass
