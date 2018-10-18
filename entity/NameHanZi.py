import uuid


class NameHanZi:
    file = ''
    hanzi = list()

    def __init__(self):
        self.__id = None
        self.__hanzi = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setHanzi(self, hanzi):
        self.__hanzi = hanzi

    def getHanzi(self):
        return self.__hanzi

    @classmethod
    def setFile(cls, file):
        cls.file = file

    @classmethod
    def readNameHanZi(cls):
        if len(NameHanZi.hanzi) > 0:
            return NameHanZi.hanzi

        file_name_hanzi = open(NameHanZi.file, encoding='utf-8')
        for line in file_name_hanzi.readlines():
            line = line.strip()

            nhz = NameHanZi()
            nhz.setId(str(uuid.uuid1()).replace('-', ''))
            nhz.setHanzi(line)

            NameHanZi.hanzi.append(nhz)
        return NameHanZi.hanzi
