import uuid


class Person:
    def __init__(self, name, sex, birthday, province, city, nation, idNumber):
        self.__id = str(uuid.uuid1()).replace('-', '')
        self.__name = name
        self.__sex = sex
        self.__birthday = birthday
        self.__province = province
        self.__city = city
        self.__nation = nation
        self.__id_number = idNumber

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def setBirthday(self, birthday):
        self.__birthday = birthday

    def getBirthday(self):
        return self.__birthday

    def setProvince(self, province):
        self.__province = province

    def getProvince(self):
        return self.__province

    def setCity(self, city):
        self.__city = city

    def getCity(self):
        return self.__city

    def setNation(self, nation):
        self.__nation = nation

    def getNation(self):
        return self.__nation

    def setIdNumber(self, idNumber):
        self.__id_number = idNumber

    def getIdNumber(self):
        return self.__id_number

    def __str__(self):
        return self.__name + "," + self.__sex + "," + self.__birthday + "," + self.__province + "," + self.__city + "," + self.__nation + "," + self.__id_number

