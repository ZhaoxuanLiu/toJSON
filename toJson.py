import simplejson as json
import pandas as pd
import numpy as np

# xlrd to read specific sheet in target excel file
file = '/Users/zhaoxuanliu/Desktop/AlgoDepth/01:28:2019/toJSON/factor_fundamental_jiaqi.xlsx'
# Use pandas to read excel sheet and convert to data frame
sheet = pd.read_excel(file, sheet_name='Sheet1')
df = pd.DataFrame(sheet)

dftmp = df.replace(np.nan, '', regex=True)




# To initialize variables
data  = {}
nlist = []

# To update the data into dictionary
for index, row in dftmp.iterrows():
        data.update({row['DBname']: {'Name': row['Name'],
                                 'Components': '',
                                 'Formula': row['Formula']}})



# To get all of column name
colnum = len(df.columns)
colName = []
colName = df.columns.values

# To use for loop to decide whether the value of specific row and column equal to 1
for index, row in dftmp.iterrows():
    for col in range(26, colnum):
        if df.iloc[index, col] == 1:
            nlist.append(colName[col])
    data[row['DBname']]['Components'] = nlist
    nlist = []




file2 = '/Users/zhaoxuanliu/Desktop/AlgoDepth/01:28:2019/toJSON/component_id.xlsx'
sheet2 = pd.read_excel(file2, sheet_name='Sheet1')
df2 = pd.DataFrame(sheet2)

dict2 = {}
tmp = []

# Put all name of components and its id in the dictionary
for index, row in df2.iterrows():
    dict2.update({row['id']:row['Name']})


for key, value in data.items():
    for i, val in enumerate(value['Components']):
        if val in dict2.values():
            print(True)
            tmp.append({list(dict2.keys())[list(dict2.values()).index(val)]: val})
        else:
            print(False)
            print(val)

    value['Components'] = []
    value['Components'] = tmp
    tmp = []

    print("####################")



# To write data in json file
j = json.dumps(data, sort_keys=False, ensure_ascii=False, indent=4)
with open('data.json', 'w') as f:
    f.write(j)



print('Programming Finished')















