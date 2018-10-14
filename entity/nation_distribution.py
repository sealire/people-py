class nation_distribution:
    def __init__(self):
        self.__id = None
        self.__nation_name = None
        self.__distribution = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setNationName(self, nation_name):
        self.__nation_name = nation_name

    def getNationName(self):
        return self.__nation_name

    def setDistribution(self, distribution):
        self.__distribution = distribution

    def getDistribution(self):
        return self.__distribution
