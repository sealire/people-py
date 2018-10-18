import random


class NameCreater:

    def __init__(self, nameHanzi, malePerfect, femalePerfect):
        self.__name_hanzi = nameHanzi
        self.__male_perfect = malePerfect
        self.__female_perfect = femalePerfect

    def creater(self, lastName, sex):
        if len(self.__name_hanzi) == 0:
            return ""

        perfect = self.__male_perfect
        if sex == '女':
            perfect = self.__female_perfect

        rand = random.random()
        while True:
            first = self.__name_hanzi[random.randint(0, len(self.__name_hanzi) - 1)].getHanzi()
            if rand < 0.4:
                first = perfect[random.randint(0, len(perfect) - 1)].getHanzi()
            if lastName != first:
                break

        second = ''
        if rand > 0.3:
            while True:
                second = self.__name_hanzi[random.randint(0, len(self.__name_hanzi) - 1)].getHanzi()
                if first != second and second != lastName:
                    break

        rand = random.random()

        name = first + second
        if rand < 0.5:
            name = second + first
        return name
