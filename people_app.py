import os

from creater.PersonCreater import *
from creater.Writer import *

dir = os.getcwd() + '/resource/'
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
    'person': dir + 'person.txt'
}

personCreater = PersonCreater(file_dir)
personCreater.init()

writer = Writer(file_dir['person'])
total = 1000000
each = 5000
for count in range(0, int(total / each)):
    persons = list()
    for num in range(0, each):
        person = personCreater.creater()
        persons.append(person)
    writer.write(persons)
    print((count + 1) * each, 'in', total)
    time.sleep(1)
