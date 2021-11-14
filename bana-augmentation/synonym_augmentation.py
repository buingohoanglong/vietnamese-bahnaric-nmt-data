from underthesea import ner
import json
from random import shuffle
import pandas as pd
from utils import format



def sent_process(text, vi_words, k=10):
    text = format(text)
    words = []
    for word, pos, _, entity in ner(text):
        if entity != "O":
            words.append([word])
        else:
            if pos in ["N", "Np", "P", "Nc"]:
                pos = "N"
            synonyms = vi_words.get(word.lower(), {}).get("syn", {}).get(pos, [word])
            if word == word.capitalize():
                if word.lower() in synonyms:
                    synonyms.remove(word.lower())
                synonyms = [s.capitalize() for s in synonyms]
            elif word == word.lower():
                if word.capitalize() in synonyms:
                    synonyms.remove(word.capitalize())
                synonyms = [s.lower() for s in synonyms]
            elif word == word.upper():
                synonyms = [s.upper() for s in synonyms]
            words.append(synonyms)
            if word not in words[-1]:
                words[-1].append(word)

    sentences = words[0]
    for candidates in words[1:]:
        _sentences = []
        for sentence in sentences:
            for word in candidates:
                new_sentence = sentence
                new_sentence += " " + word
                _sentences.append(new_sentence)
        sentences = _sentences
        shuffle(sentences)
        sentences = sentences[:k]
    sentences = list(set(sentences))
    return sentences


def main():
    vi_words = json.load(open('data_syn_processed.json', mode='r'))
    inputDir = '../data/Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/VH-TT/processed'
    outputDir = '../data/Dữ liệu cũ (Đài phát thanh Vĩnh Thạnh)/VH-TT/augment'

    invalid_words = ['Ủy ban quần chúng', 'Ủy ban dân chúng', 'mùa bầy', 'mùa bọn', 'mùa đám', 'mùa tụi', 'mùa tuồng',
        'mùa quân', 'mùa phường', 'chủ tọa Ủy ban nhân dân', 'chủ tọa Ủy ban Nhân dân', 'đào lộn hột', 
        'Ban hành kèm cặp', 'tiễn công trình', 'chống tuồng', 'đê Điều', 'chủ động Phối hợp', 
        'nghị định liên can', 'nghị định can hệ', ' Phê duyệt', ' Phối hợp', 'Hội đồng quần chúng', 
        'Hội đồng dân chúng', ' Thực hiện', 'chủ tọa UBND', 'Chủ tọa Ủy ban nhân dân', 
        'chủ tọa Ủy ban Nhân dân', 'thuộc lòng địa bàn', 'thuộc làu địa bàn', 'phai học', 'dận học',
        'Hội đồng dân chúng', 'Hội đồng quần chúng', 'Chủ tọa Hội đồng Nhân dân', 'chủ tọa Hội đồng nhân dân',
        'Nghị quyết ni', 'Quyết định ni', 'Căn cứ ni', 'chích buồng', 'chích gian', 'chích phòng', 'tiêm buồng',
        'tiêm gian', 'vi co', 'logo mác', 'logo nhãn', 'đỡ cao', 'Nghị định số phận', 'Thông tư số phận', 
        'Nghị định số mệnh', 'Thông tư số mệnh', 'Chính sách ni', 'bẩm thẩm tra số', 'thưa thẩm tra số',
        'gã công trình', 'thằng công trình', 'Gã công trình', 'Thằng công trình', 'Văn bản số mệnh', 'Văn bản số phận',
        'xịch tể', 'nhích tể', 'xích tể', 'xê tể', 'nguồn gì', 'phát triển ghét trồng trọt', 'tính sổ kinh phí', 'xịch xảy ra',
        'xê xảy ra', 'xích xảy ra', 'nhích xảy ra', 'bò gấu', 'bơ hệt', 'bò hệt', 'nguồn vốn dĩ', 'Sở hữu trí óc', 
        'kinh dinh', 'mùa vi phạm', 'dùng ghét', 'sử dụng ghét', 'số phận tiền', 'số mệnh tiền', 'heo họa xanh',
        'lợn họa xanh', 'cho thuê ghét', 'nguồn nguyên', 'nguồn vốn dĩ', 'Nguồn vốn dĩ', 'ngữ đầu tư', 'mực đầu tư', 
        'Trung tâm y tế đề phòng', 'Trung tâm y tế dự phòng', 'hoàn cảnh an toàn thực phẩm', 'cứt cấp', 'xảy vào',
        'thịt bơ', 'đi việc', 'Chủ toạ Hội đồng Nhân dân', 'chủ toạ Hội đồng nhân dân', 'Chủ toạ Ủy ban Nhân dân', 
        'chủ toạ Ủy ban nhân dân', 'chủ toạ Ủy ban Nhân dân', 'Chủ toạ Ủy ban nhân dân', 'Chủ toạ Hội đồng nhân dân',
        'chủ toạ Hội đồng Nhân dân', 'chủ toạ UBND', 'Chủ toạ UBND', 'chủ toạ HĐND', 'Chủ toạ HĐND', 'đính kèm cặp',
        'Trung tâm y tế xơ cua', 'báo đài hoa', 'báo radio', 'Sao rủi', 'Sao mun', 'kế hoạch ni', 'Kế hoạch ni',
        'huy động vốn dĩ', 'nguồn thâu', 'nác sinh hoạt', 'sinh sản rau', 'sinh sản nhau', 'sinh sản kinh doanh',
        'chuỗi sinh sản', 'Kho bạc Quốc gia', 'Kho bạc quốc gia', 'biếu thấy', 'tặng thấy', 'biếu chộ', 'tặng chộ',
        'cho chộ',
        'ương trồng', 'tháng giai đoạn', 'chọn ghét ươm trồng', 'lựa ghét ươm trồng', 'Chọn ghét ươm trồng', 
        'Lựa ghét ươm trồng', 'thoát nác', 'kim khí', 'vào rễ', 'ươm trồng trọt', 'cỏ khờ', 'cỏ ngộ', 'cỏ điên',
        'bề bướng', 'bình diện luống', 'phương diện luống', 'nác phân lân', 'mưa trường', 'thắng sản xuất', 
        'thắng sinh sản', 'hạt nảy mống', 'hột nảy mống', 'dãy bướng', 'chiều gàn', 'phát triển thường nhật',
        'năng suất làng nhàng', 'năng suất nhàng nhàng', 'phơi phóng', 'sử dụng liềm ngắt', 'sử dụng liềm bốc',
        'dùng liềm ngắt', 'dùng liềm bốc', 'Sử dụng liềm ngắt', 'Sử dụng liềm bốc', 'Dùng liềm ngắt', 
        'Dùng liềm bốc', 'nẻo vàng', 'bệnh cẩn', 'trừng trị bệnh', 'trừng trị bịnh', 'cây vầng', 'cuốn hút nhựa',
        'cuốn hút mủ', 'đánh mun', 'đánh rủi', 'làm mun', 'vào hoa', 'vào huê', 'ra huê', 'chích lòng', 'chích dạ',
        'bón cứt', 'bón lót cứt', 'vừng xui', 'vầng đen', 'vầng xui', 'vừng mun', 'vầng mun', 'nhú khỏe', 
        'Năng suất vầng', 'năng suất vầng', 'trồng vầng', 'trồng trọt vầng', 'cây vầng', 'Cây vầng', 'vàng nhạt nhẽo',
        'vàng lạnh nhạt', 'nác nóng', 'nác lạnh', 'tiệt bệnh', 'tiệt bịnh', 'cữ ngắn', 'gióng ngắn', 'dạo ngắn',
        'thoái đọt', 'Bọ cánh rắn', 'Bọ bè cứng', 'Bò bè rắn', 'Bọ phái cứng', 'Bọ phái rắn', 'bọ cánh rắn', 
        'bọ bè cứng', 'bò bè rắn', 'bọ phái cứng', 'bọ phái rắn', 'bón chia', 'Bón chia', 'trồng trọt dặm',
        'Trồng trọt dặm', 'Hom hệt', 'hom hệt', 'nhỡ cổ rễ', 'độ ẩm của ghét', 'thời đoạn phát triển', 'chùm huê',
        'thịt trái mềm mỏng', 'Thu nhặt dưới ghét', 'ống nhựa trọn', 'ống mủ trọn', 'lát ni', 'hồi ni', 'chập ni',
        'hồi này', 'chập này', 'nấm mồ hóng', 
        'gian, chống', 'buồng, chống', 'chót năm', 'co kinh nghiệm', 'thâm nhập mặn', 'tàu dãy', 'Bộ liên lạc vận tải',
        'lấp chật', 'phủ chật', 'năng lượng tái hiện',
        'dãy năm', 'tặng vay', 'dấn ủy thác', 'dìm ủy thác', 'thời gian sang', 'Thời gian sang', 'thời kì sang',
        'Thời kì sang', 'dãy năm', 'quán năm', 'mực chi', 'Mực chi', 'Buồng Kế hoach', 'Gian Kế hoạch'
        'Trung tâm giáo dục luôn', 'tiền đớp', 'tiền xơi', 'tiêu thụ khỏe',
        'tuyến lối', 'xuể lên', 'biếu biết', 'tặng biết'
    ]

    with open(f'{inputDir}/VH-TT.vi', mode='r', encoding='utf-8') as file_vi:
        with open(f'{inputDir}/VH-TT.ba', mode='r', encoding='utf-8') as file_ba:
            sentences_vi = file_vi.readlines()
            sentences_ba = file_ba.readlines()
            num_rows = len(sentences_vi)
            data = []
            for i in range(num_rows):
                vi = sentences_vi[i].strip()
                ba = sentences_ba[i].strip()
                data.append([vi, ba])
                augmented_sentences = sent_process(text=vi, vi_words=vi_words)
                for s in augmented_sentences:
                    s = format(s)
                    for w in invalid_words:
                        if s.__contains__(w):
                            break
                    else:
                        data.append([s, ba])

    df = pd.DataFrame(data, columns=['Viet', 'Bahnar']).drop_duplicates()
    df.to_csv(f'{outputDir}/VH-TT.csv', sep=',', encoding='utf-8', index=False)


if __name__ == '__main__':
    main()