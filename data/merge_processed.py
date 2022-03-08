import pandas as pd
from sklearn.model_selection import train_test_split

def merge_vi_ba(file_vi, file_ba):
    vi_sentences = open(file_vi, mode='r', encoding='utf-8').readlines()
    ba_sentences = open(file_ba, mode='r', encoding='utf-8').readlines()
    data = []
    for vi, ba in zip(vi_sentences, ba_sentences):
        vi = vi.strip()
        ba = ba.strip()
        data.append([vi, ba])
    df = pd.DataFrame(data, columns=['Viet', 'Bahnar'])
    return df

cstt = merge_vi_ba('./CS-TT/processed/CS-TT.vi', './CS-TT/processed/CS-TT.ba')
khcn = merge_vi_ba('./KH-CN/processed/KH-CN.vi', './KH-CN/processed/KH-CN.ba')
ktxh = merge_vi_ba('./KT-XH/processed/KT-XH.vi', './KT-XH/processed/KT-XH.ba')
vhtt = merge_vi_ba('./VH-TT/processed/VH-TT.vi', './VH-TT/processed/VH-TT.ba')
cstt_radio = merge_vi_ba('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/CS-TT/processed/CS-TT.vi', './Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/CS-TT/processed/CS-TT.ba')
khcn_radio = merge_vi_ba('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/KH-CN/processed/KH-CN.vi', './Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/KH-CN/processed/KH-CN.ba')
ktxh_radio = merge_vi_ba('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/KT-XH/processed/KT-XH.vi', './Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/KT-XH/processed/KT-XH.ba')
vhtt_radio = merge_vi_ba('./Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/VH-TT/processed/VH-TT.vi', './Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/VH-TT/processed/VH-TT.ba')
nsp = merge_vi_ba('./NguyenSuPhuoc/processed/data.vi', './NguyenSuPhuoc/processed/data.ba')

print(f'CS-TT: {len(cstt)}')
print(f'KH-CN: {len(khcn)}')
print(f'KT-XH: {len(ktxh)}')
print(f'VH-TT: {len(vhtt)}')
print(f'CS-TT old: {len(cstt_radio)}')
print(f'KH-CN old: {len(khcn_radio)}')
print(f'KT-XH old: {len(ktxh_radio)}')
print(f'VH-TT old: {len(vhtt_radio)}')
print(f'NSP: {len(nsp)}')

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