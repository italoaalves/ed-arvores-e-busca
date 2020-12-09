class Movie:
    def __init__(self, id, name, year):
        self.__id = id
        self.__name = name
        self.__year = year

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @id.setter
    def id(self, data):
        self.__id = data

    @name.setter
    def name(self, data):
        self.__name = data

    @year.setter
    def year(self, data):
        self.__year = data
