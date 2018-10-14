class id_number_distribution:
    def __init__(self):
        self.__id = None
        self.__province_name = None
        self.__id_number = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setProvinceName(self, province_name):
        self.__province_name = province_name

    def getProvinceName(self):
        return self.__province_name

    def setIdNumber(self, id_number):
        self.__id_number = id_number

    def getIdNumber(self):
        return self.__id_number
