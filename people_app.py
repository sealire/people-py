from entity.province import *
from entity.province_distribution import *
from entity.city import *
import uuid

home = 'F:/git/people-py/resource/'
dir = home
file_dir = {
    'province': dir + 'province.txt',
    'province_distribution': dir + 'province_distribution.txt',
    'city': dir + 'city.txt'
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
    cities = list()
    file_city = open(file_dir['city'], encoding='utf-8')
    for line in file_city.readlines():
        line = line.strip()
        line_data = line.split('\t')

        c = city()
        c.setId(str(uuid.uuid1()).replace('-', ''))
        c.setCityName(line_data[0])
        c.setProvinceName(line_data[1])

        cities.append(c)
    return cities


provinces = readProvinces()
province_distributions = readProvinceDistributions()
cities = readCities()

print(len(cities))

