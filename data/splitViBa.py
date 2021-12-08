import pandas as pd

dir = '.'

df = pd.read_csv(f'{dir}/train-synonymaugment.csv').sample(frac=1)
vi = list(df.iloc[:,0])
ba = list(df.iloc[:,1])

with open(f'{dir}/train-synonymaugment.vi', mode='w+', encoding='utf-8') as file_vi:
    with open(f'{dir}/train-synonymaugment.ba', mode='w+', encoding='utf-8') as file_ba:
        for i in range(len(vi)):
            file_vi.write(vi[i] + '\n')
            file_ba.write(ba[i] + '\n')