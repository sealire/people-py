import random


class CityCreater:

    def __init__(self, cities):
        self.__cities = cities

    def creater(self, province):
        if len(self.__cities) == 0:
            return ""

        if province in self.__cities:
            cs = self.__cities[province]
            rand = random.randint(0, len(cs) - 1)
            return cs[rand].getCityName()
        else:
            return ""
