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
    'Trung tâm y tế xơ cua'
]

dir = '../data/CS-TT/augment'
new_lines = []
with open(f'{dir}/CS-TT-new.csv', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    for l in lines:
        for w in invalid_words:
            if l.__contains__(w):
                break
        else:
            new_lines.append(l)

with open(f'{dir}/CS-TT-heuristic.csv', mode='w+', encoding='utf-8') as f:
    f.writelines(new_lines)
