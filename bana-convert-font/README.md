# bana-convert-font

## Hướng dẫn
Sử dụng hàm `handleQuoutes()` trước để xử lý các ký tự đặc biệt.\
Sau đó chạy hàm`transform2KriemNew()` để chuyển đổi dấu vành trăng khuyết.\
Kiểm tra lại dữ liệu tiếng Bana nếu có các dấu của tiếng Việt thì sử dụng replace all để loại bỏ dấu.

Lưu ý: Hàm không áp dụng được cho chữ "ĭ", cái đó phải xem bằng mắt rồi mới replace được, vì quy luật chữ "ĭ" không áp dụng được hết các truờng hợp.
