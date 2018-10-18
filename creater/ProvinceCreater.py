import random


class ProvinceCreater:

    def __init__(self, distribution):
        self.__distribution = distribution

    def creater(self):
        if len(self.__distribution) == 0:
            return ""

        rand = random.random()
        index = 0
        sum = 0
        while index < len(self.__distribution):
            sum += self.__distribution[index].getDistribution()
            if sum > rand:
                break
            index += 1

        if index < len(self.__distribution):
            return self.__distribution[index].getProvinceName()
        else:
            return self.__distribution[len(self.__distribution) - 1].getProvinceName()
