# Làm giàu dữ liệu Việt - Bana

## Hướng dẫn
Làm giàu dữ liệu bằng cách thay thế các từ có trong câu bằng một từ tương đương, có thể đồng nghĩa hoặc cùng loại từ (chủ ngữ, vị ngữ, trạng từ, tính từ). 

Ví dụ: [VI] Mình tên là Yôl\
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bana] Inh măt Yôl\
Thay từ "Mình" với các từ tương đương như "Tôi", "Tớ" ta sẽ có thêm 2 câu.\

Phần làm giàu dữ liệu chỉ có 2 hàm:
```
// Hàm bên dưới kiểm tra từ (cụm từ) có trong câu hay không.  
checkTextContainsInSentence(text, sentence);
// Hàm bên dưới bắt đầu làm giàu dữ liệu với những từ có được.
// Tham số xem cách sử dụng sẽ thấy.
augmentSentences(...);
```
Sau khi chạy xong mỗi phần phải lọc bằng mắt câu tiếng Việt để xem câu đó có nghĩa hay không, rồi mới chạy cho phần tiếp theo. Có một vài câu có thể có quy luật thay thế thì mới chạy code được ở các hàm bên dưới:
```
handleNumberList(); 
handleThingsList();
```

## Cách sử dụng

Mình sẽ có các mảng dữ liệu như bên dưới :
```
people_list_vi = ["Kinh", "Ba na", "Chăm"]
people_list_bana = ["Kinh", "Bơhnar", "Chăm"]
...
```
Chạy hàm `augmentSentences(...);` để làm giàu dữ liệu
Hiện mình đã chạy cho tới phần `bird_list`. Các bạn có thể tiếp tục phần sau hoặc nếu muốn chạy lại từ đầu cũng được. \
Nhớ là mỗi lần chạy xong nhớ phải kiểm tra dữ liệu xem câu có nghĩa hay không để lọc rồi mới chạy phần tiếp theo, mình có đoạn print `...Converted sentence is...` ra các phần làm giàu ở hàm augmentSentences, nếu thấy câu nào không đúng thì tìm kiếm trong file output để loại bỏ câu đó (bỏ câu sai bên tiếng Việt và Bana tương ứng).

Lưu ý: Chạy từng theo thứ tự các mảng để lọc từng phần, lúc đó dữ liệu ít sẽ dễ dàng lọc hơn là chạy một lượt rồi lọc.
Có phần mình comment `can not use` là vì sau khi chạy xong mình thấy không sử dụng được nên skip mảng đó.
