from entity.province import *
from entity.province_distribution import *
import uuid

home = {
    'province': 'F:/people/province.txt',
    'province_distribution': 'F:/people/province_distribution.txt'
}
file_dir = home


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


provinces = readProvinces()
province_distributions = readProvinceDistributions()

print(len(province_distributions))

