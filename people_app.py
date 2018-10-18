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

from creater.ProvinceCreater import *
from creater.CityCreater import *
from creater.SexCreater import *
from creater.BirthdayCreater import *
from creater.NationCreater import *
from creater.IdNumberCreater import *
from creater.LastNameCreater import *

home = 'F:/git/people-py/resource/'
work = 'D:/py/people-py/resource/'
dir = home
file_dir = {
    'province': dir + 'province.txt',
    'province_distribution': dir + 'province_distribution.txt',
    'city': dir + 'city.txt',
    'sex': dir + 'sex.txt',
    'age_distribution': dir + 'age_distribution.txt',
    'nation': dir + 'nation.txt',
    'nation_distribution': dir + 'nation_distribution.txt',
    'last_name': dir + 'last_name.txt',
    'last_name_distribution': dir + 'last_name_distribution.txt',
    'id_number_distribution': dir + 'id_nubmer_distribution.txt',
    'name_hanzi': dir + 'name_hanzi.txt',
    'male_perfect': dir + 'male_perfect.txt',
    'female_perfect': dir + 'female_perfect.txt',
}

Province.setFile(file_dir['province'])
provinces = Province.readProvince()
ProvinceDistribution.setFile(file_dir['province_distribution'])
ProvinceDistribution.setProvinces(provinces)
provinceDs = ProvinceDistribution.readDistribution()
provinceCreater = ProvinceCreater(provinceDs)
province = provinceCreater.creater()
print(province)

City.setFile(file_dir['city'])
City.setProvinces(provinces)
cities = City.readCity(province)
cityCreater = CityCreater(cities)
city = cityCreater.creater()
print(city)

Sex.setFile(file_dir['sex'])
sexes = Sex.readSex()
sexCreater = SexCreater(sexes)
sex = sexCreater.creater()
print(sex)

AgeDistribution.setFile(file_dir['age_distribution'])
ageDs = AgeDistribution.readDistribution()
birthdayCreater = BirthdayCreater(ageDs)
birthday = birthdayCreater.creater()
print(birthday)

Nation.setFile(file_dir['nation'])
nations = Nation.readNation()
NationDistribution.setFile(file_dir['nation_distribution'])
NationDistribution.setNations(nations)
nationDs = NationDistribution.readDistribution()
nationCreater = NationCreater(nationDs)
nation = nationCreater.creater()
print(nation)

IdNumberDistribution.setFile(file_dir['id_number_distribution'])
IdNumberDistribution.setProvinces(provinces)
idNumbers = IdNumberDistribution.readDistribution(province)
idNumberCreater = IdNumberCreater(idNumbers)
idNumber = idNumberCreater.creater(birthday, sex)
print(idNumber)

LastName.setFile(file_dir['last_name'])
lastNames = LastName.readLastName()
LastNameDistribution.setFile(file_dir['last_name_distribution'])
LastNameDistribution.setLastNames(lastNames)
top100 = LastNameDistribution.readLastNameTop100()
other = LastNameDistribution.readOtherLastName()
lastNameCreater = LastNameCreater(top100, other)
lastName = lastNameCreater.creater()
print(lastName)

# print()
# for city in cities:
#     print(city.getCityName(), end=" ")
