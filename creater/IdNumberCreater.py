import random


class IdNumberCreater:

    def __init__(self, id_numbers):
        self.__id_numbers = id_numbers

    def creater(self, birthday, sex):
        if len(self.__id_numbers) == 0:
            return ""

        rand = random.randint(0, len(self.__id_numbers) - 1)

        birthday = birthday.replace('-', '')

        sexes = [0, 2, 4, 6, 8]
        ss = sexes[random.randint(0, 4)]
        if sex == '男':
            ss += 1
        police = 9 + random.randint(1, 90)

        return self.__id_numbers[rand] + birthday + str(police) + str(ss) + str(random.randint(0, 9))
