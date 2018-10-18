import uuid


class NationDistribution:
    file = ''
    nations = list()
    distribution = list()

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

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def setNations(cls, nations):
        cls.nations = nations

    @classmethod
    def readDistribution(cls):
        if len(NationDistribution.distribution) > 0:
            return NationDistribution.distribution

        natonMap = {}
        for naton in NationDistribution.nations:
            natonMap[naton.getNationName()] = naton

        file_nation_distribution = open(NationDistribution.file, encoding='utf-8')
        for line in file_nation_distribution.readlines():
            line = line.strip()
            line_data = line.split('\t')

            nd = NationDistribution()
            nd.setId(str(uuid.uuid1()).replace('-', ''))
            nation = line_data[0]
            if natonMap[nation] is None:
                raise Exception('no nation: ', nation)
            nd.setNationName(nation)
            nd.setDistribution(float(line_data[1]))

            NationDistribution.distribution.append(nd)
        return NationDistribution.distribution
