import string
from sys import argv

script_name, cols_count, rows_count = argv
cols_count = int(cols_count)
rows_count = int(rows_count)
col_names = list(string.ascii_lowercase)

try:
    if cols_count > len(col_names):
        print(f'ERROR: Columns count can not be more than {len(col_names)}!')
        print('INFO: Programm will stop now. Restart with correct number of columns.')
        exit()

except ValueError:
    print("There are must be 2 args. Use in command line: 'python <script_name.py> <cols_count> <rows_count>")
    exit()


class Table:

    def __init__(self, cols_count, rows_count):

        self.col_names = col_names
        self.rows_count = rows_count
        self.cols_count = cols_count
        self.base_struct = [[]]

        for i in range(self.cols_count):
            self.base_struct[0].insert(i, self.col_names[i])

        self.base_struct[0].insert(0, ' ')

        for i in range(self.rows_count):
            self.base_struct.append([])

        for i in range(1, len(self.base_struct)):
            self.base_struct[i].append(i)
            for j in range(self.cols_count):
                self.base_struct[i].append('_')

    def print_table(self):

        for i in range(len(self.base_struct)):
            print(self.base_struct[i], '\n')


obj = Table(cols_count, rows_count)
obj.print_table()