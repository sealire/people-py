import random


class CityCreater:

    def __init__(self, cities):
        self.__cities = cities

    def creater(self):
        if len(self.__cities) == 0:
            return ""

        rand = random.randint(0, len(self.__cities) - 1)
        return self.__cities[rand].getCityName()
