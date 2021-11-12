import pandas as pd

dir = './Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/VH-TT'

df = pd.read_csv(f'{dir}/VH-TT.csv')
vi = list(df.iloc[:,0])
ba = list(df.iloc[:,1])

with open(f'{dir}/VH-TT.vi', mode='w+', encoding='utf-8') as file_vi:
    with open(f'{dir}/VH-TT.ba', mode='w+', encoding='utf-8') as file_ba:
        for i in range(len(vi)):
            file_vi.write(vi[i] + '\n')
            file_ba.write(ba[i] + '\n')