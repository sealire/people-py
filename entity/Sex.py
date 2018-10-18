import uuid


class Sex:
    file = ''
    sexes = list()

    def __init__(self):
        self.__id = None
        self.__code = None
        self.__name = None
        self.__distribution = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setCode(self, code):
        self.__code = code

    def getCode(self):
        return self.__code

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setDistribution(self, distribution):
        self.__distribution = distribution

    def getDistribution(self):
        return self.__distribution

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def readSex(cls):
        if len(Sex.sexes) > 0:
            return Sex.sexes

        file_sex = open(Sex.file, encoding='utf-8')
        for line in file_sex.readlines():
            line = line.strip()
            line_data = line.split('\t')

            s = Sex()
            s.setId(str(uuid.uuid1()).replace('-', ''))
            s.setCode(line_data[0])
            s.setName(line_data[1])
            s.setDistribution(float(line_data[2]))

            Sex.sexes.append(s)
        return Sex.sexes
