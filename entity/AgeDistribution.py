import uuid


class AgeDistribution:
    file = ''
    distribution = list()

    def __init__(self):
        self.__id = None
        self.__min_age = None
        self.__max_age = None
        self.__distribution = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setMinAge(self, min_age):
        self.__min_age = min_age

    def getMinAge(self):
        return self.__min_age

    def setMaxAge(self, max_age):
        self.__max_age = max_age

    def getMaxAge(self):
        return self.__max_age

    def setDistribution(self, distribution):
        self.__distribution = distribution

    def getDistribution(self):
        return self.__distribution

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def readDistribution(cls):
        if len(AgeDistribution.distribution) > 0:
            return AgeDistribution.distribution

        file_age_distribution = open(AgeDistribution.file, encoding='utf-8')
        for line in file_age_distribution.readlines():
            line = line.strip()
            line_data = line.split('\t')

            ad = AgeDistribution()
            ad.setId(str(uuid.uuid1()).replace('-', ''))
            ad.setMinAge(int(line_data[0]))
            ad.setMaxAge(int(line_data[1]))
            ad.setDistribution(float(line_data[2]))

            AgeDistribution.distribution.append(ad)
        return AgeDistribution.distribution
