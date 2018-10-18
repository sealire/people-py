import uuid


class Nation:
    file = ''
    nations = list()

    def __init__(self):
        self.__id = None
        self.__nation_name = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setNationName(self, nation_name):
        self.__nation_name = nation_name

    def getNationName(self):
        return self.__nation_name

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def readNation(cls):
        if len(Nation.nations) > 0:
            return Nation.nations

        file_nation = open(Nation.file, encoding='utf-8')
        for line in file_nation.readlines():
            line = line.strip()
            line_data = line.split('\t')

            p = Nation()
            p.setId(str(uuid.uuid1()).replace('-', ''))
            p.setNationName(line_data[0])

            Nation.nations.append(p)
        return Nation.nations