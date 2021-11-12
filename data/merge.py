import pandas as pd
from os import listdir, sep
from os.path import isfile, join

from pandas.core.reshape.merge import merge

path = './Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/CS-TT/origin/'
files = [f for f in listdir(path) if isfile(join(path, f))]
print(files)

concat_df = None
for f in files:
    df = pd.read_csv(path + f)
    if concat_df is None:
        concat_df = df.iloc[:,1:]
    else:
        concat_df = pd.concat([concat_df, df.iloc[:,1:]])

concat_df.to_csv(f'./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/CS-TT/CS-TT.csv', sep=',', encoding='utf-8', index=False)
