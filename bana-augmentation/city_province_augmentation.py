# import pandas as pd

# df = pd.read_csv('./Danh sách quận huyện Việt Nam 2021 Full - ©DiaOcThongThai.Com.csv')

# # print(df[['Tỉnh Thành', 'Quận Huyện']])

# print(df['Tỉnh Thành'].values)


from underthesea import ner

text = 'Tôi sống ở huyện Vĩnh Thạnh được 10 năm'

print(ner(text))