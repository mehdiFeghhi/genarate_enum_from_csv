import csv


def make_row(name, value):
    return ['   ', f'{name}', ' ', '=', ' ', f'{value}', '\n']


def make_top_name(name):
    return ['class', ' ', f'{name}', '(', 'Enum', ')', ':' + '\n']

def make_python_file_of_enum(dict_of_enum: dict):
    list_of_item = ['from', ' ', 'enum', ' ', 'import', ' ', 'Enum', '\n']

    for keys in dict_of_enum.keys():
        list_of_item += make_top_name(keys)
        for attribute in dict_of_enum[keys].keys():
            list_of_item += make_row(attribute.replace(' ','_').replace('-','_'), dict_of_enum[keys][attribute])

    txt = ''.join(list_of_item)
    f = open('enum_class.py', "w")
    f.write(txt)
    f.close()


def make_csv_to_dict(csv_read):
    dic_res = {}

    for row in csv_read:
        if dic_res.get(row[0]) is None:
            dic_res[row[0]] = {row[1]: row[2]}
        else:
            dic_res[row[0]].update({row[1]: row[2]})

    return dic_res

if __name__ == '__main__':
    file = open('فیلدهای deep socre enum - Sheet1.csv')
    dict_of_item = make_csv_to_dict(csv.reader(file))
    #print(dict_of_item)
    make_python_file_of_enum(dict_of_item)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
