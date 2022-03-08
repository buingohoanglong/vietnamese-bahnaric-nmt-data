from utils import format, no_accent_vietnamese
from underthesea import ner

def capitalize(text):
    return text[0].capitalize() + text[1:]

def main():
    vi_sentences = open('../data/train-synonymaugment.vi', mode='r', encoding='utf-8').readlines()
    ba_sentences = open('../data/train-synonymaugment.ba', mode='r', encoding='utf-8').readlines()

    with open('../data/train-synonymaugment-accent.vi', mode='w+', encoding='utf-8') as file_vi:
        with open('../data/train-synonymaugment-accent.ba', mode='w+', encoding='utf-8') as file_ba:
            vi_new = []
            ba_new = []
            for vi, ba in zip(vi_sentences, ba_sentences):
                vi = format(vi)
                ba = format(ba)
                for word_vi, _, _, ne in ner(vi):
                    if ne in ['B-PER', 'I-PER', 'B-LOC', 'I-LOC', 'B-ORG', 'I-ORG'] and word_vi == capitalize(word_vi):
                        word_no_accent = no_accent_vietnamese(word_vi)
                        if word_no_accent in ba:
                            ba = ba.replace(word_no_accent, word_vi)
                print(vi)
                print(ba)
                print()
                vi_new.append(vi + '\n')
                ba_new.append(ba + '\n')
            file_vi.writelines(vi_new)
            file_ba.writelines(ba_new)



if __name__ == '__main__':
    main()