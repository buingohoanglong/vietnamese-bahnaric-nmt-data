import pandas as pd
from sklearn.model_selection import train_test_split

cstt = pd.read_csv('./CS-TT/augment/CS-TT.csv')
khcn = pd.read_csv('./KH-CN/augment/KH-CN.csv')
ktxh = pd.read_csv('./KT-XH/augment/KT-XH.csv')
vhtt = pd.read_csv('./VH-TT/augment/VH-TT.csv')
cstt_radio = pd.read_csv('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/CS-TT/augment/CS-TT.csv')
khcn_radio = pd.read_csv('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/KH-CN/augment/KH-CN.csv')
ktxh_radio = pd.read_csv('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/KT-XH/augment/KT-XH.csv')
vhtt_radio = pd.read_csv('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/VH-TT/augment/VH-TT.csv')
nsp = pd.read_csv('./NguyenSuPhuoc-augmented/augment/data.csv')

print(len(cstt))
print(len(khcn))
print(len(ktxh))
print(len(vhtt))
print(len(cstt_radio))
print(len(khcn_radio))
print(len(ktxh_radio))
print(len(vhtt_radio))
print(len(nsp))

final = pd.concat([cstt, khcn, ktxh, vhtt, cstt_radio, khcn_radio, ktxh_radio, vhtt_radio, nsp]).dropna().drop_duplicates()

print(f'--|Final: {len(final)}')

train_vi, test_valid_vi, train_ba, test_valid_ba = train_test_split(final['Viet'], final['Bahnar'], test_size=0.3, shuffle=True)
test_vi, valid_vi, test_ba, valid_ba = train_test_split(test_valid_vi, test_valid_ba, test_size=0.5, shuffle=True)

print(f'--|Train: {len(train_vi)}, {len(train_ba)}')
print(f'--|Test: {len(test_vi)}, {len(test_ba)}')
print(f'--|Valid: {len(valid_vi)}, {len(valid_ba)}')

def write_to_file(df, path):
    with open(path, mode='w+', encoding='utf-8') as f:
        for line in df:
            f.write(line + '\n')

write_to_file(train_vi, './train.vi')
write_to_file(train_ba, './train.ba')
write_to_file(test_vi, './test.vi')
write_to_file(test_ba, './test.ba')
write_to_file(valid_vi, './valid.vi')
write_to_file(valid_ba, './valid.ba')