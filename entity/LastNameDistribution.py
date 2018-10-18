import uuid


class LastNameDistribution:
    file = ''
    lastNames = list()
    top100_distribution = list()
    other_lastName = list()

    def __init__(self):
        self.__id = None
        self.__last_name = None
        self.__distribution = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setLastName(self, last_name):
        self.__last_name = last_name

    def getLastName(self):
        return self.__last_name

    def setDistribution(self, distribution):
        self.__distribution = distribution

    def getDistribution(self):
        return self.__distribution

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def setLastNames(cls, lastNames):
        cls.lastNames = lastNames

    @classmethod
    def readLastNameTop100(cls):
        if len(LastNameDistribution.top100_distribution) == 0:
            LastNameDistribution.readLastName()
        return LastNameDistribution.top100_distribution

    @classmethod
    def readOtherLastName(cls):
        if len(LastNameDistribution.top100_distribution) == 0:
            LastNameDistribution.readLastName()
        return LastNameDistribution.other_lastName

    @classmethod
    def readLastName(self):
        lastNameMap = {}
        for lastName in LastNameDistribution.lastNames:
            lastNameMap[lastName.getLastName()] = lastName

        top100 = set()
        file_last_name_distribution = open(LastNameDistribution.file, encoding='utf-8')
        for line in file_last_name_distribution.readlines():
            line = line.strip()
            line_data = line.split('\t')

            lnd = LastNameDistribution()
            lnd.setId(str(uuid.uuid1()).replace('-', ''))
            lastName = line_data[0]
            if lastNameMap[lastName] is None:
                raise Exception('no lastName: ', lastName)
            lnd.setLastName(lastName)
            lnd.setDistribution(float(line_data[1]))

            LastNameDistribution.top100_distribution.append(lnd)
            top100.add(lastName)

        lnset = set()
        for ln in LastNameDistribution.lastNames:
            lnset.add(ln)

        lnset = lnset - top100
        for ln in lnset:
            LastNameDistribution.other_lastName.append(ln)
