

train_vi = open('./origin/train.vi', mode='r', encoding='utf-8').readlines()
train_ba = open('./origin/train.ba', mode='r', encoding='utf-8').readlines()
test_vi = open('./origin/test.vi', mode='r', encoding='utf-8').readlines()
test_ba = open('./origin/test.ba', mode='r', encoding='utf-8').readlines()
valid_vi = open('./origin/valid.vi', mode='r', encoding='utf-8').readlines()
valid_ba = open('./origin/valid.ba', mode='r', encoding='utf-8').readlines()

data_vi = train_vi + test_vi + valid_vi
data_ba = train_ba + test_ba + valid_ba

data_vi_new = []
data_ba_new = []
for vi, ba in zip(data_vi, data_ba):
    if vi in data_vi_new or vi.strip() == '' or ba.strip() == '':
        continue
    data_vi_new.append(vi)
    data_ba_new.append(ba)

print(len(data_vi), len(data_ba))
print(len(data_vi_new), len(data_ba_new))

with open('./processed/data.vi', mode='w+', encoding='utf-8') as file_vi:
    file_vi.writelines(data_vi_new)

with open('./processed/data.ba', mode='w+', encoding='utf-8') as file_ba:
    file_ba.writelines(data_ba_new)

