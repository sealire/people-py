import random


class LastNameCreater:

    def __init__(self, top100_distribution, other_lastName):
        self.__top100_distribution = top100_distribution
        self.__other_lastName = other_lastName

    def creater(self):
        if len(self.__top100_distribution) == 0:
            return ""

        rand = random.random()
        index = 0
        sum = 0
        while True:
            sum += self.__top100_distribution[index].getDistribution()
            if sum > rand or index >= len(self.__top100_distribution):
                break
            index += 1

        if index < len(self.__top100_distribution):
            return self.__top100_distribution[index].getLastName()
        else:
            return self.__other_lastName[random.randint(0, len(self.__other_lastName) - 1)]
