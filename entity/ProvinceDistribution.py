import uuid


class ProvinceDistribution:
    file = ''
    provinces = list()
    distribution = list()

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

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def setProvinces(cls, provinces):
        cls.provinces = provinces

    @classmethod
    def readDistribution(cls):
        if len(ProvinceDistribution.distribution) > 0:
            return ProvinceDistribution.distribution

        provinceMap = {}
        for province in ProvinceDistribution.provinces:
            provinceMap[province.getProvinceName()] = province

        file_province_distribution = open(ProvinceDistribution.file, encoding='utf-8')
        for line in file_province_distribution.readlines():
            line = line.strip()
            line_data = line.split('\t')

            pd = ProvinceDistribution()
            pd.setId(str(uuid.uuid1()).replace('-', ''))
            province = line_data[0]
            if provinceMap[province] is None:
                raise Exception('no province: ', province)
            pd.setProvinceName(province)
            pd.setDistribution(float(line_data[1]))

            ProvinceDistribution.distribution.append(pd)
        return ProvinceDistribution.distribution
