import random


class SexCreater:

    def __init__(self, sexes):
        self.__sexes = sexes

    def creater(self):
        if len(self.__sexes) == 0:
            return ""

        rand = random.random()
        if rand < self.__sexes[0].getDistribution():
            return self.__sexes[0].getName()
        else:
            return self.__sexes[1].getName()
