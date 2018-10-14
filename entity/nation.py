class nation:
    def __init__(self):
        self.__id = None
        self.__nation_name = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setNationName(self, nation_name):
        self.__nation_name = nation_name

    def getNationName(self):
        return self.__nation_name
