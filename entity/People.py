class People:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__sex = None
        self.__birthday = None
        self.__nation = None
        self.__register_province = None
        self.__register_city = None
        self.__live_province = None
        self.__live_city = None
        self.__create_datetime = None
        self.__update_datetime = None

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

    def setNation(self, nation):
        self.__nation = nation

    def getNation(self):
        return self.__nation

    def setRegisterProvince(self, register_province):
        self.__register_province = register_province

    def getRegisterProvince(self):
        return self.__register_province

    def setRegisterCity(self, register_city):
        self.__register_city = register_city

    def getRegisterCity(self):
        return self.__register_city

    def setLiveProvince(self, live_province):
        self.__live_province = live_province

    def getLiveProvince(self):
        return self.__live_province

    def setLiveCity(self, live_city):
        self.__live_city = live_city

    def getLiveCity(self):
        return self.__live_city

    def setCreateDatetime(self, create_datetime):
        self.__create_datetime = create_datetime

    def getCreateDatetime(self):
        self.__create_datetime

    def setUpdate_datetime(self, update_datetime):
        self.__update_datetime = update_datetime

    def getUpdate_datetime(self):
        return self.__update_datetime

    def convertOutFormat(self):
        return self.__id + '\t' + self.__name + '\t' + str(self.__sex) + '\t' + self.__birthday + '\t' + self.__nation \
               + '\t' + self.__register_province + '\t' + self.__register_city + '\t' + self.__live_province \
               + '\t' + self.__live_city + '\t' + str(self.__create_datetime) + '\t' + str(self.__update_datetime)
