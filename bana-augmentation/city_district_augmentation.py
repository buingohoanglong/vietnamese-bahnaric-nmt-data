import pandas as pd
import re
from underthesea import ner
from random import shuffle

def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảã]', 'a', s)
    s = re.sub(r'[ấầậẩẫ]', 'â', s)
    s = re.sub(r'[ắằặẳẵ]', 'ă', s)
    s = re.sub(r'[ÀÁẠẢÃ]', 'A', s)
    s = re.sub(r'[ẦẤẬẨẪ]', 'Â', s)
    s = re.sub(r'[ẰẮẶẲẴ]', 'Ă', s)
    s = re.sub(r'[èéẹẻẽ]', 'e', s)
    s = re.sub(r'[ềếệểễ]', 'ê', s)
    s = re.sub(r'[ÈÉẸẺẼ]', 'E', s)
    s = re.sub(r'[ỀẾỆỂỄ]', 'Ê', s)
    s = re.sub(r'[òóọỏõ]', 'o', s)
    s = re.sub(r'[ồốộổỗ]', 'ô', s)
    s = re.sub(r'[ờớợởỡ]', 'ơ', s)
    s = re.sub(r'[ÒÓỌỎÕ]', 'O', s)
    s = re.sub(r'[ỒỐỘỔỖ]', 'Ô', s)
    s = re.sub(r'[ỜỚỢỞỠ]', 'Ơ', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũ]', 'u', s)
    s = re.sub(r'[ừứựửữ]', 'ư', s)
    s = re.sub(r'[ÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỪỨỰỬỮ]', 'Ư', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    return s

def format(text):
    text = re.sub(f"  ", " ", text)
    text = re.sub(f"_", " ", text)
    text = re.sub(f" \.", ".", text)
    text = re.sub(f"' ", "'", text)
    text = re.sub(f" ,", ",", text)
    text = re.sub(f" ;", ";", text)
    text = re.sub(f" %", "%", text)
    text = re.sub(f" :", ":", text)
    text = re.sub(f" !", "!", text)
    text = re.sub(f" \?", "?", text)
    text = re.sub(f"\( ", "(", text)
    text = re.sub(f" \)", ")", text)
    text = re.sub(f" / ", "/", text)
    text = re.sub(f"\" ", "\"", text)
    text = re.sub(f" \"", "\"", text)
    text = re.sub(f" g ", "g ", text)
    text = re.sub(f" kg ", "kg ", text)
    text = re.sub(f" m ", "m ", text)
    text = re.sub(f" cm ", "cm ", text)
    text = re.sub(f" m2 ", "m2 ", text)
    text = re.sub(f" ha ", "ha ", text)
    return text.strip()

def augment(dict, vi, ba, k=5):
    vi = format(vi)
    ba = format(ba)
    pairs = []
    for word_vi, _, _, _ in ner(vi):
        if word_vi in dict and dict[word_vi] in ba:
            for key in dict:
                if key == word_vi:
                    continue
                pairs.append([vi.replace(word_vi, key), ba.replace(dict[word_vi], dict[key])])
            shuffle(pairs)
            pairs = pairs[:k-1]
    pairs.insert(0, [vi, ba])
    return pairs

def city_district_augment(cities, districts, vi, ba, k=5):
    pairs = []
    for vi_augment, ba_augment in augment(districts, vi, ba, k=k):
        pairs += augment(cities, vi_augment, ba_augment)
    original_pair = pairs[0]
    pairs = pairs[1:]
    shuffle(pairs)
    return [original_pair] + pairs[:k-1]
    

def main():
    df = pd.read_csv('./Danh sách quận huyện Việt Nam 2021 Full - ©DiaOcThongThai.Com.csv')

    cities = list(set(df['Tỉnh Thành'].values))
    districts = list(set([
        p.replace('Quận ', '').replace('Huyện ', '').replace('Thị xã ', '').replace(' (tỉnh lỵ)', '').replace('Thành phố ', '') 
        for p in list(set(df['Quận Huyện'].values)) if re.search('\d', p) is None
    ]))

    cities = {c:no_accent_vietnamese(c) for c in cities}
    districts = {p:no_accent_vietnamese(p) for p in districts}

    vi_sentences = open('../data/test.vi', mode='r', encoding='utf-8').readlines()
    ba_sentences = open('../data/test.ba', mode='r', encoding='utf-8').readlines()
    with open('../data/test-augment.vi', mode='w+', encoding='utf-8') as file_vi:
        with open('../data/test-augment.ba', mode='w+', encoding='utf-8') as file_ba:
            for vi, ba in zip(vi_sentences, ba_sentences):
                pairs = city_district_augment(cities, districts, vi, ba)
                for vi, ba in pairs:
                    file_vi.write(vi + '\n')
                    file_ba.write(ba + '\n')
                    print(vi)
                    print(ba)
                    print()


if __name__ == '__main__':
    main()