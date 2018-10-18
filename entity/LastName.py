import uuid


class LastName:
    file = ''
    lastNames = list()

    def __init__(self):
        self.__id = None
        self.__last_name = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setLastName(self, last_name):
        self.__last_name = last_name

    def getLastName(self):
        return self.__last_name

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def readLastName(cls):
        if len(LastName.lastNames) > 0:
            return LastName.lastNames

        file_last_name = open(LastName.file, encoding='utf-8')
        for line in file_last_name.readlines():
            line = line.strip()
            line_data = line.split('\t')

            p = LastName()
            p.setId(str(uuid.uuid1()).replace('-', ''))
            p.setLastName(line_data[0])

            LastName.lastNames.append(p)
        return LastName.lastNames
