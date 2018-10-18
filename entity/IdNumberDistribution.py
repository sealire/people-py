import uuid


class IdNumberDistribution:
    file = ''
    provinces = list()
    distribution = {}

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

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def setProvinces(cls, provinces):
        cls.provinces = provinces

    @classmethod
    def readDistribution(cls):
        if len(IdNumberDistribution.distribution) == 0:
            provinceMap = {}
            for province in IdNumberDistribution.provinces:
                provinceMap[province.getProvinceName()] = province

            distribution = list()
            file_id_distribution = open(IdNumberDistribution.file, encoding='utf-8')
            for line in file_id_distribution.readlines():
                line = line.strip()
                line_data = line.split('\t')

                ind = IdNumberDistribution()
                ind.setId(str(uuid.uuid1()).replace('-', ''))
                province = line_data[0]
                if provinceMap[province] is None:
                    raise Exception('no province: ', province)
                ind.setProvinceName(province)
                ind.setIdNumber(line_data[1])

                distribution.append(ind)

            for d in distribution:
                ids = d.getIdNumber().split(',')
                lids = list()
                for id in ids:
                    lids.append(id)

                IdNumberDistribution.distribution[d.getProvinceName()] = lids

        return IdNumberDistribution.distribution
