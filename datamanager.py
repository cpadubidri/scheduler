import pandas as pd


class DataManager:
    
    def __init__(self, debug=False):
        '''
        Initializes the DataManager class.
        '''
        self.debug = debug
        self.__version__ = '0.1.0'
        self.developername = 'Jyoti'

    def read_file(self, path):
        '''
        Reads the input file based on its extension. Currently supports CSV and SQL files.
        '''
        try:
            if path.endswith('.csv'): # Check if the file extension is .csv
                return self.__readcsv__(path) # Read the CSV file
            elif path.endswith('.sql'): # Check if the file extension is .sql
                return self.__readsql__(path) # Read the SQL file
            elif path.endswith('.json'):
                return self.__readjson__(path)
            else:
                # If the file is not CSV or SQL, it's considered unsupported
                raise ValueError('Input file type is not supported')
        except ValueError as err:
            # Catch the ValueError and print the error message
            print(err)
            return 0

    def __readcsv__(self, path, encoding='utf-16'):
        '''
        Reads a CSV file and returns its content.
        '''
        data = pd.read_csv(path)
        return data


    def __readsql__(self, path):
        '''
        Reads a SQL file and returns its content.
        '''
        pass
    
    def __readjson__(self, path):
        '''
        Read a JSON file and returns its content.
        '''
        data = pd.read_json(path)
        return data
    



if __name__=='__main__':
    dh = DataManager(debug=True)
    # print(dh.developername)
    # data = dh.read_file(path='assets\eventdata.csv') 
    # print(f' Read file using read_file {len(data)}')


    # data2 = dh.__readcsv__(path='assets\eventdata.csv', encoding='utf-16')
    # print(f' Read file using read_csv {len(data)}')


    