

banakriem_sentence_vi = open('./origin/vi_0504_s.txt', mode='r', encoding='utf-8').readlines()
banakriem_sentence_ba = open('./origin/bana_0504_s.txt', mode='r', encoding='utf-8').readlines()
banakriem_word_vi = open('./origin/vi_0504_w.txt', mode='r', encoding='utf-8').readlines()
banakriem_word_ba = open('./origin/bana_0504_w.txt', mode='r', encoding='utf-8').readlines()
radio_vi = open('./origin/lang-vi-radio.txt', mode='r', encoding='utf-8').readlines()
radio_ba = open('./origin/bana-vni2unicode-new.txt', mode='r', encoding='utf-8').readlines()

data_vi = banakriem_sentence_vi + banakriem_word_vi + radio_vi
data_ba = banakriem_sentence_ba + banakriem_word_ba + radio_ba

data_vi_new = []
data_ba_new = []
for vi, ba in zip(data_vi, data_ba):
    vi = vi.strip()
    ba = ba.strip()
    data_vi_new.append(vi)
    data_ba_new.append(ba)

print(f'Bahnar Kriem sentence: {len(banakriem_sentence_vi)}')
print(f'Bahnar Kriem word: {len(banakriem_word_vi)}')
print(f'Radio: {len(radio_vi)}')
print(f'NSP total: {len(data_vi_new)}')

with open('./processed/data.vi', mode='w+', encoding='utf-8') as file_vi:
    for vi in data_vi_new:
        file_vi.write(vi + '\n')

with open('./processed/data.ba', mode='w+', encoding='utf-8') as file_ba:
    for ba in data_ba_new:
        file_ba.write(ba + '\n')

