import pandas as pd


class DataManager:
    
    def __init__(self, debug=False):
        self.debug = debug

    def read_file(self, path):
        try:
            if path.endswith('.csv'):
                return self.__readcsv__(path)
            elif path.endswith('.sql'):
                return self.__readsql__(path)
            else:
                raise ValueError('Input file type is not supported')
        except ValueError as err:
            print(err)
            return 0

    def __readcsv__(self, path, encoding='utf-16'):
        pass


    def __readsql__(self, path):
        pass


if __name__=='__main__':
    dh = DataManager(debug=True)
    data = dh.read_file('assets/scheduler-dummy-data.csv') 
    print(data)