class province_distribution:
    def __init__(self):
        self.__id = None
        self.__province_name = None
        self.__distribution = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setProvinceName(self, province_name):
        self.__province_name = province_name

    def getProvinceName(self):
        return self.__province_name

    def setDistribution(self, distribution):
        self.__distribution = distribution

    def getDistribution(self):
        return self.__distribution
