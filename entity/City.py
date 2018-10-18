import uuid


class City:
    file = ''
    provinces = list()
    cities = list()

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

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def setProvinces(cls, provinces):
        cls.provinces = provinces

    @classmethod
    def readCity(cls, p=None):
        if len(City.cities) == 0:
            provinceMap = {}
            for province in City.provinces:
                provinceMap[province.getProvinceName()] = province

            file_city = open(City.file, encoding='utf-8')
            for line in file_city.readlines():
                line = line.strip()
                line_data = line.split('\t')

                c = City()
                c.setId(str(uuid.uuid1()).replace('-', ''))
                c.setCityName(line_data[0])
                province = line_data[1]
                if provinceMap[province] is None:
                    raise Exception('no province: ', province)
                c.setProvinceName(province)

                City.cities.append(c)

        if p is None:
            return City.cities
        else:
            cities = list()
            for city in City.cities:
                if city.getProvinceName() == p:
                    cities.append(city)
            return cities
