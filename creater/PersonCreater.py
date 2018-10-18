from entity.Province import *
from entity.ProvinceDistribution import *
from entity.City import *
from entity.Sex import *
from entity.AgeDistribution import *
from entity.Nation import *
from entity.NationDistribution import *
from entity.IdNumberDistribution import *
from entity.LastName import *
from entity.LastNameDistribution import *
from entity.NameHanZi import *
from entity.MalePerfectHanZi import *
from entity.FemalePerfectHanZi import *
from entity.Person import *

from creater.ProvinceCreater import *
from creater.CityCreater import *
from creater.SexCreater import *
from creater.BirthdayCreater import *
from creater.NationCreater import *
from creater.IdNumberCreater import *
from creater.LastNameCreater import *
from creater.NameCreater import *


class PersonCreater:
    def __init__(self, files):
        self.__files = files
        self.__provinceCreater = None
        self.__cityCreater = None
        self.__sexCreater = None
        self.__birthdayCreater = None
        self.__nationCreater = None
        self.__idNumberCreater = None
        self.__lastNameCreater = None
        self.__nameCreater = None

    def init(self):
        Province.setFile(self.__files['province'])
        provinces = Province.readProvince()
        ProvinceDistribution.setFile(self.__files['province_distribution'])
        ProvinceDistribution.setProvinces(provinces)
        provinceDs = ProvinceDistribution.readDistribution()
        self.__provinceCreater = ProvinceCreater(provinceDs)

        City.setFile(self.__files['city'])
        City.setProvinces(provinces)
        cities = City.readCity()
        self.__cityCreater = CityCreater(cities)

        Sex.setFile(self.__files['sex'])
        sexes = Sex.readSex()
        self.__sexCreater = SexCreater(sexes)

        AgeDistribution.setFile(self.__files['age_distribution'])
        ageDs = AgeDistribution.readDistribution()
        self.__birthdayCreater = BirthdayCreater(ageDs)

        Nation.setFile(self.__files['nation'])
        nations = Nation.readNation()
        NationDistribution.setFile(self.__files['nation_distribution'])
        NationDistribution.setNations(nations)
        nationDs = NationDistribution.readDistribution()
        self.__nationCreater = NationCreater(nationDs)

        IdNumberDistribution.setFile(self.__files['id_number_distribution'])
        IdNumberDistribution.setProvinces(provinces)
        idNumbers = IdNumberDistribution.readDistribution()
        self.__idNumberCreater = IdNumberCreater(idNumbers)

        LastName.setFile(self.__files['last_name'])
        lastNames = LastName.readLastName()
        LastNameDistribution.setFile(self.__files['last_name_distribution'])
        LastNameDistribution.setLastNames(lastNames)
        top100 = LastNameDistribution.readLastNameTop100()
        other = LastNameDistribution.readOtherLastName()
        self.__lastNameCreater = LastNameCreater(top100, other)

        NameHanZi.setFile(self.__files['name_hanzi'])
        nameHanzis = NameHanZi.readNameHanZi()
        MalePerfectHanZi.setFile(self.__files['male_perfect'])
        malePerfect = MalePerfectHanZi.readPerfect()
        FemalePerfectHanZi.setFile(self.__files['female_perfect'])
        femalePerfect = FemalePerfectHanZi.readPerfect()
        self.__nameCreater = NameCreater(nameHanzis, malePerfect, femalePerfect)

    def creater(self):
        province = self.__provinceCreater.creater()
        city = self.__cityCreater.creater(province)
        sex = self.__sexCreater.creater()
        birthday = self.__birthdayCreater.creater()
        nation = self.__nationCreater.creater()
        idNumber = self.__idNumberCreater.creater(birthday, sex, province)
        lastName = self.__lastNameCreater.creater()
        name = self.__nameCreater.creater(lastName, sex)
        person = Person(str(lastName) + str(name), sex, birthday, province, city, nation, idNumber)
        return person
