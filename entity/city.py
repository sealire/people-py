class city:
    def __init__(self):
        self.__id = None
        self.__city_code = None
        self.__city_name = None
        self.__province = None
        self.__province_name = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setCityCode(self, city_code):
        self.__city_code = city_code

    def getCityCode(self):
        return self.city_code

    def setCityName(self, city_name):
        self.__city_name = city_name

    def getCityName(self):
        return self.__city_name

    def setProvince(self, province):
        self.__province = province

    def getProvince(self):
        return self.__province

    def setProvinceName(self, province_name):
        self.__province_name = province_name

    def getProvinceName(self):
        return self.__province_name
