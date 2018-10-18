import uuid


class FemalePerfectHanZi:
    file = ''
    perfect = list()

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
    def readPerfect(cls):
        if len(FemalePerfectHanZi.perfect) > 0:
            return FemalePerfectHanZi.perfect

        file_name_hanzi = open(FemalePerfectHanZi.file, encoding='utf-8')
        for line in file_name_hanzi.readlines():
            line = line.strip()

            mphz = FemalePerfectHanZi()
            mphz.setId(str(uuid.uuid1()).replace('-', ''))
            mphz.setHanzi(line)

            FemalePerfectHanZi.perfect.append(mphz)
        return FemalePerfectHanZi.perfect
