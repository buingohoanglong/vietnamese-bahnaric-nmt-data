import random

vocative_list_subject_self_vi = ["Tôi", "Mình", "Tớ "]
vocative_list_subject_self_bana = ["Inh", "Inh", "Inh "]

vocative_list_subject_upper_vi = ["Ba", "Bố", "Mẹ", "Má", "Cô", "Dì", "Chú", "Bác", "Dượng", "Dượng", "Ông", "Bà",
                                  "Anh", "Anh trai", "Chị gái", "Chị",
                                  "Anh rể", "Thím", "Mợ", "Cậu"]
vocative_list_subject_upper_bana = ["'Bă", "'Bă", "Mĭ", "Mĭ", "Duch", "Duch", "Ma", "Mih", "'Bă 'băn", "'Bă yăng", "'Bok", "Yă",
                                    "'Nhŏng", "'Nhŏng", "Mai", "Mai",
                                    "Mi", "Duch", "Duch", "Ma"]

people_list_vi = ["Kinh", "Ba na", "Chăm"]
people_list_bana = ["Kinh", "Bơhnar", "Chăm"]

time_list_adverb_vi = ["Hôm nay", "Ngày hôm nay", "Buổi sáng", "Buổi chiều", "Buổi tối", "Ngày mai", "Ngày kia",
                       "Bình minh", "Lúc trước", "Lúc nãy", "Lúc đó", "Khi đó", "Lúc đầu", "Hoàng hôn", "Sáng sớm",
                       "Hôm kia",
                       "Ngày hôm kia", "Xế trưa", "Hôm kìa", "Hôm kỉa", "Hôm nọ", "Bây giờ", "Hiện nay", "Sáng nay", "Buổi sáng", "Năm sau"]
time_list_adverb_bana = ["'Năr adrơ̆u", "'Năr adrơ̆u", "Bơgê", "Jơnang kơsơ̆", "Jơnang kơ'măng", "'Năr dơning", "'Năr dơnuônh",
                         "Bơgê", "Jơnang adrol sơ̆", "Jơnang 'noh hĕi", "Jơnang 'noh", "Jơnang 'noh", "Jơdnang pơtơm", "'Năr mưt", "Bơgê sruôih",
                         "'Năr iơ̆u",
                         "'Năr iơ̆u", "'Năr jrang", "'Năr tơman", "'Năr tơmĕt", "'Năr yơ ơ̆u", "Ahrĕi ơ̆u", "Ahrĕi ơ̆u",
                         "Bơgê", "Trong bơgê", "Sơnăm anô̆"]

number_list_vi = ["Một", "1", "Hai", "2", "Ba", "3", "Bốn", "4", "Năm", "5", "Sáu", "6", "Bảy", "7", "Tám", "8", "Chín",
                  "9", "Mười", "10", "Một ngàn", "1000", "Một trăm", "100"]
number_list_bana = ["Minh", "1", "'Bal", "2", "Pêng", "3", "Puôn", "4", "Đăm", "5", "Dơdrơ̆u", "6", "Tơpơh", "7",
                    "Tơhngam", "8", "Sĭn",
                    "9", "Minh jĭt", "10", "Minh abơ̆u", "1000", "Minh hriêng", "100"]

action_talk_list_vi = ["Hỏi", "Đáp lời", "Đáp", "Trả lời", "Trả lời"]
action_talk_list_bana = ["Apinh", "Tơ'bơ̆l", "Tơ'bơ̆l", "Akhan ăn", "Tơ'bơ̆l"]

universe_things_list_vi = ["Mặt trời", "Mặt trăng", "Ngôi sao", "Sao mai", "Sao hôm"]
universe_things_list_bana = ["Măt 'năr", "Măt khăi", "Sơnglŏng", "Sơnglŏng bơgê", "Sơnglŏng tong măng"]

color_list_vi = ["Màu tím", "Màu trắng", "Tím", "Trắng", "Màu vàng", "Vàng", "Màu xanh", "Xanh", "Màu đỏ", "Đỏ",
                 "Màu đen", "Đen"]
color_list_bana = ["Yưm", "'Bak", "Yưm", "'Bak", "'Brơ̆u", "'Brơ̆u", "Kơsĕ", "Kơsĕ", "Gôh", "Gôh",
                   "Găm", "Găm"]

use_things_list_vi = ["Quần áo", "Áo", "Quần", "Dao rựa", "Dao phát", "Dao", "Cái kéo", "Kéo"]
use_things_list_bana = ["Kuơ̆n au", "Au", "Kuơ̆n", "Dơbưk", "Dơbưk muih", "Săng", "Săng chơkep", "Săng chơkep"]

animal_list_vi = ["Trâu", "Gà", "Lợn", "Chó", "Ngựa", "Con ngựa", "Vịt", "Cá", "Dê", "Chim", "Mèo rừng", "Mèo", "Khỉ"]
animal_list_bana = ["Kơpô", "'Yer", "Nhŭng", "Kŏ", "Aseh", "Aseh", "Ada", "Ka", "Bơbê", "Sem", "Meu bri", "Meu", "Đŏk"]

bird_list_vi = ["Chim sáo", "Con sáo", "Vẹt", "Con vẹt", "Bồ câu", "Chim bồ câu", "Vành khuyên", "Chim vành khuyên",
                "Chim sẻ", "Con sẻ", "Chim sẻ", "Con sẻ", "Bói cá", "Chim bói cá", "Diều hâu", "Chim diều hâu",
                "Chim cu", "Chim công", "Én", "Chim én",
                "Chim phượng hoàng", "Phượng hoàng", "Cú mèo", "Chim cú mèo"]
bird_list_bana = ["Chơrau", "Chơrau", "Sem diê̆", "Sem diê", "Kơtơp", "Kơtơp", "Sem blang kĕi", "Sem blang kĕi",
                  "Sem chap", "Sem chap", "Sem prum", "Sem prum", "Sem hlum", "Sem hlum", "Sem klang", "Sem klang",
                  "Sem kơtơp", "Sem kơwơng", "Pơsel yang yai", "Yang yai",
                  "Sem kring", "Sem kring", "Sem lơ-oh", "Sem lơ-oh"]


### ============================== TỪ ĐÂY XUỐNG DƯỚI CHƯA CHẠY ============================
vocative_list_subject_normal_vi = ["Em", "Mày", "Con", "Cháu"]
vocative_list_subject_normal_bana = ["Oh", "Ih", "Kon", "Mon"]

body_list_vi = ["Mắt", "Miệng", "Mồm", "Miệng", "Mồm", "Tay", "Chân"]
body_list_bana = ["Măt", "'Bơ̆l", "'Bơ̆r", "'Bơ̆l", "'Bơ̆r", "Ti", "Jưng"]

fruit_list_vi = ["Chanh", "Chanh", "Bưởi", "Cam", "Quýt", "Chuối lùn", "Chuối tiêu", "Chuối", "Ớt"]
fruit_list_bana = ["Kruôĭ chanh", "Chanh", "Kruôĭ 'bŏng", "Kruôĭ 'ngam", "Kruôĭ 'ngam", "Pit pha", "Pit pdơnang", "Pit",
                   "Amrĕ"]

measure_list_vi = ["km", "cây số", "Mét"]
measure_list_bana = ["kơ̆i sô̆", "kơ̆i sô̆", "Met"]

plant_list_vi = ["Trúc", "Cây trúc", "Tre"]
plant_list_bana = ["Kram yai", "Kram yai", "Kram"]

direction_list_vi = ["Phía dưới", "Dưới", "Phía trên", "Trên", "Phía sau", "Sau", "Bên trái", "Bên phải", "Bên phải"]
direction_list_bana = ["Ala", "Ala", "Nhơ̆i", "Nhơ̆i", "Đưng rŏng", "Đưng rŏng", "'Miêu", "Gah 'ma", "'Ma"]

characteristic_list_vi = ["Độc ác", "Chân thật", "Thật thà", ]
characteristic_list_bana = ["Brư̆ kơnĕ", "Tơpăt klak", "Tơpăt klak", ]

week_day_list_vi = []
week_day_list_bana = []


def checkTextContainsInSentence(text=None, sentence=None):
    if text is None or sentence is None:
        return False, False
    if text.__contains__(' ') is False:
        splitWords = sentence.split(' ')
        sSize = len(splitWords)
        for i in range(sSize):
            if splitWords[i] == text.lower():
                return False, True
            elif splitWords[i] == text:
                return splitWords[i] == text, False
    else:
        if sentence.__contains__(' ' + text.lower() + ' ') or \
                sentence.__contains__(
                ' ' + text.lower() + '.') or \
                sentence.__contains__(' ' + text.lower() + ',') or \
                sentence.__contains__(' ' + text.lower() + '\n') or \
                sentence.__contains__(' ' + text.lower() + '"'):
            return False, True
        else:
            return sentence.__contains__(text), False
    return False, False


def augmentSentences(groupListVi=None, groupListBana=None, inputDir='.', outputDir='.', txtVi=None, txtBana=None,
                    outputViName=None, outputBanaName=None):
    if groupListVi is None or len(groupListVi) == 0:
        return
    if groupListBana is None or len(groupListBana) == 0:
        return
   
    txtViFile = open(f'{inputDir}/{txtVi}', encoding='utf-8', errors='ignore').read()
    txtBanaFile = open(f'{inputDir}/{txtBana}', encoding='utf-8', errors='ignore').read()

    txtViAugments = open(f'{inputDir}/data_vi_augmentation.txt', encoding='utf-8', errors='ignore').read()
    txtBanaAugments = open(f'{inputDir}/data_bana_augmentation.txt', encoding='utf-8', errors='ignore').read()

    splitsVi = txtViFile.split('\n')
    splitsBana = txtBanaFile.split('\n')
    num_rows = len(splitsVi)

    for i in range(num_rows):
        currentRowVi = splitsVi[i]
        currentRowBana = splitsBana[i]

        txtViAugments += currentRowVi + '\n'
        txtBanaAugments += currentRowBana + '\n'

        groupSize = len(groupListVi)
        sameGroupPos = -1
        shouldUseLowerText = False

        for j in range(groupSize):
            resTextVi, resLowerTextVi = checkTextContainsInSentence(groupListVi[j], currentRowVi)
            resTextBana, resLowerTextBana = checkTextContainsInSentence(groupListBana[j], currentRowBana)
            if (resTextVi == True and resTextBana == True) or (resLowerTextVi == True and resLowerTextBana == True):
                sameGroupPos = j
                shouldUseLowerText = resLowerTextVi == True
                break

        if sameGroupPos != -1:
            print('-=-=-=============================')
            print('[VI] Original sentence is ', currentRowVi)
            # print('[BANA] Original sentence is ', currentRowBana)
            for k in range(groupSize):
                if k != sameGroupPos:
                    if shouldUseLowerText is True:
                        txtViAugments += currentRowVi.replace(groupListVi[sameGroupPos].lower().strip(),
                                                              groupListVi[k].lower().strip()) + '\n'
                        print('[VI] Converted sentence is ',
                              currentRowVi.replace(groupListVi[sameGroupPos].lower().strip(),
                                                   groupListVi[k].lower().strip()))
                        txtBanaAugments += currentRowBana.replace(groupListBana[sameGroupPos].lower().strip(),
                                                                  groupListBana[k].lower().strip()) + '\n'
                        # print('[BANA] Converted sentence is ', currentRowBana.replace(groupListBana[sameGroupPos], groupListBana[k]))
                    else:
                        txtViAugments += currentRowVi.replace(groupListVi[sameGroupPos].strip(),
                                                              groupListVi[k].strip()) + '\n'
                        print('[VI] Converted sentence is ',
                              currentRowVi.replace(groupListVi[sameGroupPos].strip(), groupListVi[k].strip()))
                        txtBanaAugments += currentRowBana.replace(groupListBana[sameGroupPos].strip(),
                                                                  groupListBana[k].strip()) + '\n'
                        # print('[BANA] Converted sentence is ', currentRowBana.replace(groupListBana[sameGroupPos], groupListBana[k]))

    with open(f'{outputDir}/{outputViName}', mode='w', encoding='utf-8') as f:
        f.write(txtViAugments)
    with open(f'{outputDir}/{outputBanaName}', mode='w', encoding='utf-8') as f:
        f.write(txtBanaAugments)


def handleNumberList():
    inputsDir = 'inputs_old'
    # txtVi = "data_vi_spr.txt"
    # txtBana = "data_bana_spr.txt"
    txtViFile = open(inputsDir + '/' + 'number_list_vi.txt', encoding='utf-8', errors='ignore').read()
    txtBanaFile = open(inputsDir + '/' + 'number_list_bana.txt', encoding='utf-8', errors='ignore').read()

    txtViFile = txtViFile.replace(' mười mươi ', ' mười ').replace(' 10 mươi ', ' 10 ').replace(' một ngàn mươi ', ' một ngàn ').replace(' 1000 mươi ', ' 1000 ').replace(' một trăm mươi ', ' một trăm ').replace(' 100 mươi ', ' 100 ').replace(' 1 mươi ', ' 1 ').replace(' một mươi ', ' mười ')
    txtBanaFile = txtBanaFile.replace(' minh jĭt jĭt ', ' minh jĭt ').replace(' 10 jĭt ', ' 10 ').replace(' minh abơ̆u jĭt ', ' minh abơ̆u ').replace(' 1000 jĭt ', ' 1000 ').replace(' minh hriêng jĭt ', ' minh hriêng ').replace(' 100 jĭt ', ' 100 ').replace(' 1 jĭt ', ' 1 ')

    txtViFile = txtViFile.replace('quân', 'quần').replace('đi chợ bán cải', 'đi chợ bán củi')

    with open(inputsDir + '/' + 'number_list_vi_new.txt', 'w', encoding='utf-8') as f:
        f.write(txtViFile)
    with open(inputsDir + '/' + 'number_list_bana_new.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaFile)


def handleThingsList():
    inputsDir = 'inputs_old'
    # txtVi = "data_vi_spr.txt"
    # txtBana = "data_bana_spr.txt"
    txtViFile = open(inputsDir + '/' + 'use_things_list_vi.txt', encoding='utf-8', errors='ignore').read()
    txtBanaFile = open(inputsDir + '/' + 'use_things_list_bana.txt', encoding='utf-8', errors='ignore').read()

    txtViFile = txtViFile.replace('một con quần áo', 'một bộ quần áo').replace('một con quần', 'một cái quần').replace('một con áo', 'một cái áo').replace('con cái kéo', 'cái kéo').replace('con kéo', 'cái kéo').replace('mặc bộ áo trắng', 'mặc cái áo trắng').replace('mặc bộ quần trắng', 'mặc cái quần trắng')
    txtBanaFile = txtBanaFile.replace('hlak kuơ̆n au piêu', 'bô̆ kuơ̆n au piêu').replace('mỉnh', 'minh')

    txtViFile = txtViFile.replace('Yôl nhìn thấy một phụ nữ mặc bộ dao rựa trắng', 'Yôl nhìn thấy một phụ nữ cầm con dao rựa trắng')
    txtBanaFile = txtBanaFile.replace('Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng srơ̆p dơbưk kok', 'Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng jil dơbưk kok')

    txtViFile = txtViFile.replace('Yôl nhìn thấy một phụ nữ mặc bộ dao phát trắng', 'Yôl nhìn thấy một phụ nữ mang con dao phát trắng')
    txtBanaFile = txtBanaFile.replace('Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng srơ̆p dơbưk muih kok', 'Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng jil dơbưk muih kok')

    txtViFile = txtViFile.replace('Yôl nhìn thấy một phụ nữ mặc bộ dao trắng', 'Yôl nhìn thấy một phụ nữ mang con dao trắng')
    txtBanaFile = txtBanaFile.replace('Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng srơ̆p săng kok', 'Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng jil săng kok')

    txtViFile = txtViFile.replace('Yôl nhìn thấy một phụ nữ mặc bộ cái kéo trắng', 'Yôl nhìn thấy một phụ nữ mang cái kéo trắng')
    txtBanaFile = txtBanaFile.replace('Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng srơ̆p săng chơkep kok', 'Yôl ngŏ \'boh minh \'nu mai kon kơdiŏng jil dăng chơkep kok')

    txtViFile = txtViFile.replace('Yôl nhìn thấy một phụ nữ mặc bộ kéo trắng', 'Yôl nhìn thấy một phụ nữ mang cái kéo trắng')

    txtViFile = txtViFile.replace('tháng một, tháng một một, tháng một hai.', 'tháng mười, tháng mười một, tháng mười hai.')
    txtBanaFile = txtBanaFile.replace('khĕi minh, khĕi minh minh, khĕi minh \'bal.', 'tháng mười, tháng mười một, tháng mười hai.')
    # splitsVi = txtViFile.split('\n')
    # splitsBana = txtBanaFile.split('\n')
    # num_rows = len(splitsVi)
    # txtViFileNew = ''
    # txtBanaFileNew = ''
    #
    # for i in range(num_rows):
    #     rowVi = splitsVi[i]
    #     if rowVi.__contains__('Yôl nhìn thấy một phụ nữ mặc bộ dao rựa trắng'):
    #         txtViFileNew += 'Yôl nhìn thấy một phụ nữ cầm con dao rựa trắng' + '\n'
    #         txtBanaFileNe +=
    #     elif rowVi.__contains__('')

    with open(inputsDir + '/' + 'use_things_list_vi_new.txt', 'w', encoding='utf-8') as f:
        f.write(txtViFile)
    with open(inputsDir + '/' + 'use_things_list_bana_new.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaFile)


def handleQuoutes():
    inputsDir = 'inputs_old'
    outputDir = 'new_output'
    txtVi = "bird_list_vi.txt"
    txtBana = "bird_list_bana.txt"
    txtViFile = open(inputsDir + '/' + txtVi, encoding='utf-8', errors='ignore').read()
    txtBanaFile = open(inputsDir + '/' + txtBana, encoding='utf-8', errors='ignore').read()

    txtViFile = txtViFile.replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("\n ", "\n")
    txtBanaFile = txtBanaFile.replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("\n ", "\n")
    with open(outputDir + '/bird_list_vi.txt', 'w', encoding='utf-8') as f:
        f.write(txtViFile)
    with open(outputDir + '/bird_list_bana.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaFile)


def handleEndSentence():
    inputsDir = 'new_output'
    outputDir = 'new_output'
    txtVi = "bird_list_vi.txt"
    txtBana = "bird_list_bana.txt"
    txtViFile = open(inputsDir + '/' + txtVi, encoding='utf-8', errors='ignore').read()
    txtBanaFile = open(inputsDir + '/' + txtBana, encoding='utf-8', errors='ignore').read()

    splitsVi = txtViFile.split('\n')
    splitsBana = txtBanaFile.split('\n')
    num_rows = len(splitsVi)

    txtViFileNew = ""
    txtBanaFileNew = ""

    for i in range(num_rows):
        if splitsVi[i].endswith(".") and (not splitsBana[i].endswith(".")):
            txtViFileNew += splitsVi[i] + "\n"
            txtBanaFileNew += splitsBana[i] + "." + "\n"
        elif splitsBana[i].endswith(".") and (not splitsVi[i].endswith(".")):
            txtBanaFileNew += splitsBana[i] + "\n"
            txtViFileNew += splitsVi[i] + "." + "\n"

    with open(outputDir + '/bird_list_vi_1.txt', 'w', encoding='utf-8') as f:
        f.write(txtViFileNew)
    with open(outputDir + '/bird_list_bana_1.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaFileNew)


def shuffleRandomSentences():
    inputsDir = 'new_output'
    txtVi = "use_things_list_vi_new.txt"
    txtBana = "use_things_list_bana_new.txt"
    txtViFile = open(inputsDir + '/' + txtVi, encoding='utf-8', errors='ignore').read()
    txtBanaFile = open(inputsDir + '/' + txtBana, encoding='utf-8', errors='ignore').read()

    splitsVi = txtViFile.split('\n')
    splitsBana = txtBanaFile.split('\n')
    num_rows = len(splitsVi)

    generalArr = list(zip(splitsVi, splitsBana))
    random.shuffle(generalArr)
    splitsVi, splitsBana = zip(*generalArr)

    txtViFileNew = ""
    txtBanaFileNew = ""
    splitsVi = list(splitsVi)
    splitsBana = list(splitsBana)

    for i in range(num_rows):
        txtViFileNew += splitsVi[i].strip() + "\n"
        txtBanaFileNew += splitsBana[i].strip() + "\n"

    with open(inputsDir + '/use_things_list_vi_new_shuffle.txt', 'w', encoding='utf-8') as f:
        f.write(txtViFileNew)
    with open(inputsDir + '/use_things_list_bana_new_shuffle.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaFileNew)

### Cách sử dụng: Mở comment và chạy thứ tự từng phần một

# augmentSentences(groupListVi=vocative_list_subject_self_vi, groupListBana=vocative_list_subject_self_bana,
#                  txtVi="data_vi_spr.txt", txtBana="data_bana_spr.txt",
#                  outputViName="vocative_list_subject_self_vi.txt", outputBanaName="vocative_list_subject_self_bana.txt")

# augmentSentences(groupListVi=vocative_list_subject_upper_vi, groupListBana=vocative_list_subject_upper_bana,
#                  txtVi="vocative_list_subject_self_vi.txt", txtBana="vocative_list_subject_self_bana.txt",
#                  outputViName="vocative_list_subject_upper_vi.txt",
#                  outputBanaName="vocative_list_subject_upper_bana.txt")

# augmentSentences(groupListVi=people_list_vi, groupListBana=people_list_bana,
#                  txtVi="vocative_list_subject_upper_vi.txt", txtBana="vocative_list_subject_upper_bana.txt",
#                  outputViName="people_list_vi.txt",
#                  outputBanaName="people_list_bana.txt")

# augmentSentences(groupListVi=time_list_adverb_vi, groupListBana=time_list_adverb_bana,
#                  txtVi="people_list_vi.txt", txtBana="people_list_bana.txt",
#                  outputViName="time_list_adverb_vi.txt",
#                  outputBanaName="time_list_adverb_bana.txt")

# augmentSentences(groupListVi=number_list_vi, groupListBana=number_list_bana,
#                  txtVi="time_list_adverb_vi.txt", txtBana="time_list_adverb_bana.txt",
#                  outputViName="number_list_vi.txt",
#                  outputBanaName="number_list_bana.txt")

# handleNumberList()

# augmentSentences(groupListVi=action_talk_list_vi, groupListBana=action_talk_list_bana,
#                  txtVi="number_list_vi_new.txt", txtBana="number_list_bana_new.txt",
#                  outputViName="action_talk_list_vi.txt",
#                  outputBanaName="action_talk_list_bana.txt")

#### Can not use
# augmentSentences(groupListVi=measure_list_vi, groupListBana=measure_list_bana,
#                  txtVi="action_talk_list_vi.txt", txtBana="action_talk_list_bana.txt",
#                  outputViName="measure_list_vi.txt",
#                  outputBanaName="measure_list_bana.txt")

# augmentSentences(groupListVi=universe_things_list_vi, groupListBana=universe_things_list_bana,
#                  txtVi="action_talk_list_vi.txt", txtBana="action_talk_list_bana.txt",
#                  outputViName="universe_things_list_vi.txt",
#                  outputBanaName="universe_things_list_bana.txt")

# augmentSentences(groupListVi=color_list_vi, groupListBana=color_list_bana,
#                  txtVi="universe_things_list_vi.txt", txtBana="universe_things_list_bana.txt",
#                  outputViName="color_list_vi.txt",
#                  outputBanaName="color_list_bana.txt")

# augmentSentences(groupListVi=use_things_list_vi, groupListBana=use_things_list_bana,
#                  txtVi="color_list_vi.txt", txtBana="color_list_bana.txt",
#                  outputViName="use_things_list_vi.txt",
#                  outputBanaName="use_things_list_bana.txt")

# augmentSentences(groupListVi=animal_list_vi, groupListBana=animal_list_bana,
#                  txtVi="vi-1903.txt", txtBana="bana-1903.txt",
#                  outputViName="animal_list_vi.txt",
#                  outputBanaName="animal_list_bana.txt")

# augmentSentences(groupListVi=bird_list_vi, groupListBana=bird_list_bana,
#                  txtVi="animal_list_vi.txt", txtBana="animal_list_bana.txt",
#                  outputViName="bird_list_vi.txt",
#                  outputBanaName="bird_list_bana.txt")
# handleThingsList()
# handleQuoutes()
handleEndSentence()
# shuffleRandomSentences()
