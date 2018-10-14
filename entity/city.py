class city:
    def __init__(self):
        self.__id = None
        self.__province_code = None
        self.__province_name = None
        self.__province_short_name = None
        self.__capital = None
        self.__capital_name = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setProvinceCode(self, province_code):
        self.__province_code = province_code

    def getProvinceCode(self):
        return self.__province_code

    def setProvinceName(self, province_name):
        self.__province_name = province_name

    def getProvinceName(self):
        return self.__province_name

    def setProvinceShortName(self, province_short_name):
        self.__province_short_name = province_short_name

    def getProvinceShortName(self):
        return self.__province_short_name

    def setCapital(self, __capital):
        self.__capital = __capital

    def getCapital(self):
        return self.__capital

    def setCapitalName(self, capital_name):
        self.__capital_name = capital_name

    def getCapitalName(self):
        return self.__capital_name
