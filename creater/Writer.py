class Writer:
    def __init__(self, file):
        self.__file = file

    def write(self, persons):
        fout = open(self.__file, 'a+', encoding='utf-8')
        for person in persons:
            fout.write(str(person) + '\n')
        fout.close
