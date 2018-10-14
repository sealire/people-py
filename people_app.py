from entity.province import *
from entity.province_distribution import *
from entity.city import *
from entity.nation import *
from entity.nation_distribution import *
from entity.last_name import *
import uuid

home = 'F:/git/people-py/resource/'
dir = home
file_dir = {
    'province': dir + 'province.txt',
    'province_distribution': dir + 'province_distribution.txt',
    'city': dir + 'city.txt',
    'nation': dir + 'nation.txt',
    'nation_distribution': dir + 'nation_distribution.txt',
    'last_name': dir + 'last_name.txt'
}


def readProvinces():
    provinces = list()
    file_province = open(file_dir['province'], encoding='utf-8')
    for line in file_province.readlines():
        line = line.strip()
        line_data = line.split('\t')

        p = province()
        p.setId(str(uuid.uuid1()).replace('-', ''))
        p.setProvinceName(line_data[0])
        p.setProvinceShortName(line_data[1])

        provinces.append(p)
    return provinces


def readProvinceDistributions():
    provinceMap = {}
    for province in provinces:
        provinceMap[province.getProvinceName()] = province

    province_distributions = list()
    file_province_distribution = open(file_dir['province_distribution'], encoding='utf-8')
    for line in file_province_distribution.readlines():
        line = line.strip()
        line_data = line.split('\t')

        pd = province_distribution()
        pd.setId(str(uuid.uuid1()).replace('-', ''))
        province = line_data[0]
        if provinceMap[province] is None:
            raise Exception('no province: ', province)
        pd.setProvinceName(province)
        pd.setDistribution(line_data[1])

        province_distributions.append(pd)
    return province_distributions

def readCities():
    provinceMap = {}
    for province in provinces:
        provinceMap[province.getProvinceName()] = province

    cities = list()
    file_city = open(file_dir['city'], encoding='utf-8')
    for line in file_city.readlines():
        line = line.strip()
        line_data = line.split('\t')

        c = city()
        c.setId(str(uuid.uuid1()).replace('-', ''))
        c.setCityName(line_data[0])
        province = line_data[1]
        if provinceMap[province] is None:
            raise Exception('no province: ', province)
        c.setProvinceName(province)

        cities.append(c)
    return cities

def readNations():
    nations = list()
    file_nation = open(file_dir['nation'], encoding='utf-8')
    for line in file_nation.readlines():
        line = line.strip()

        n = nation()
        n.setId(str(uuid.uuid1()).replace('-', ''))
        n.setNationName(line)

        nations.append(n)
    return nations

def readNationDistributions():
    natinMap = {}
    for nation in nations:
        natinMap[nation.getNationName()] = nation

    nation_distributions = list()
    file_nation_distributions = open(file_dir['nation_distribution'], encoding='utf-8')
    for line in file_nation_distributions.readlines():
        line = line.strip()
        line_data = line.split('\t')

        nd = nation_distribution()
        nd.setId(str(uuid.uuid1()).replace('-', ''))
        nation = line_data[0]
        if natinMap[nation] is None:
            raise Exception('no nation: ', nation)
        nd.setNationName(nation)
        nd.setDistribution(line_data[1])

        nation_distributions.append(nd)
    return nation_distributions

def readLastNames():
    last_names = list()
    file_last_name = open(file_dir['last_name'], encoding='utf-8')
    for line in file_last_name.readlines():
        line = line.strip()

        n = last_name()
        n.setId(str(uuid.uuid1()).replace('-', ''))
        n.setLastName(line)

        last_names.append(n)
    return last_names


provinces = readProvinces()
province_distributions = readProvinceDistributions()
cities = readCities()
nations = readNations()
nation_distributions = readNationDistributions()
last_names = readLastNames()

for province in provinces:
    print(province.getProvinceName(), end=" ")

print()
for city in cities:
    print(city.getCityName(), end=" ")

print()
for nation in nations:
    print(nation.getNationName(), end=" ")

print()
for last_name in last_names:
    print(last_name.getLastName(), end=" ")
