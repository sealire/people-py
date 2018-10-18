import random
import time, datetime


class BirthdayCreater:

    def __init__(self, distribution):
        self.__distribution = distribution

    def creater(self):
        if len(self.__distribution) == 0:
            return ""

        age = self.getAge()
        date_time = datetime.datetime.now()
        date_time = date_time + datetime.timedelta(days=-365 * age)
        date_time = datetime.datetime(date_time.year, 1, 1, 0, 0, 0, 0)
        rand = random.randint(0, 365)
        date_time = date_time + datetime.timedelta(days=+rand)
        return date_time.strftime('%Y-%m-%d')


    def getAge(self):
        min = 0
        max = 0
        rand = random.random()
        index = 0
        sum = 0
        while True:
            sum += self.__distribution[index].getDistribution()
            if sum > rand or index >= len(self.__distribution):
                break
            index += 1

        if index < len(self.__distribution):
            min = self.__distribution[index].getMinAge()
            max = self.__distribution[index].getMaxAge()
        else:
            min = self.__distribution[len(self.__distribution) - 1].getMaxAge()
            max = 120

        return random.randint(min, max - 1)
