import pandas as pd


class DataManager:
    
    def __init__(self, debug=False):
        '''
        Initializes the DataManager class.
        '''
        self.debug = debug

    def read_file(self, path):
        '''
        Reads the input file based on its extension. Currently supports CSV and SQL files.
        '''
        try:
            if path.endswith('.csv'): # Check if the file extension is .csv
                return self.__readcsv__(path) # Read the CSV file
            elif path.endswith('.sql'): # Check if the file extension is .sql
                return self.__readsql__(path) # Read the SQL file
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
        pass


    def __readsql__(self, path):
        '''
        Reads a SQL file and returns its content.
        '''
        pass


if __name__=='__main__':
    dh = DataManager(debug=True)
    data = dh.read_file('assets/scheduler-dummy-data.csv') 
    print(data)