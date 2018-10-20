import uuid


class Person:
    def __init__(self, lastName, firstName, sex, birthday, province, city, nation, idNumber):
        self.__id = str(uuid.uuid1()).replace('-', '')
        self.__last_name = lastName
        self.__first_name = firstName
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

    def setLastName(self, lastName):
        self.__last_name = lastName

    def getLastName(self):
        return self.__last_name

    def setFirstName(self, firstName):
        self.__first_name = firstName

    def getFirstName(self):
        return self.__first_name

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
        return self.__last_name + "," + self.__first_name + "," + self.__sex + "," + self.__birthday + "," \
               + self.__province + "," + self.__city + "," + self.__nation + "," + self.__id_number

