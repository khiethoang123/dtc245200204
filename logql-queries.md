# TÀI LIỆU HƯỚNG DẪN TRUY VẤN LOG BẰNG LOGQL TRÊN GRAFANA LOKI
## MÔN: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM - ĐỀ TÀI 3

- **Sinh viên thực hiện**: Đặng Trần Hưng (MSSV: 20210001)
- **Hệ thống**: Loki 2.9.4 + Promtail 2.9.4 + Nginx 1.27 + WordPress 6.7

---

## 📌 1. GIỚI THIỆU VỀ LOGQL
**LogQL (Log Query Language)** là ngôn ngữ truy vấn mạnh mẽ của Grafana Loki, lấy cảm hứng từ cú pháp của PromQL trong Prometheus. LogQL được chia thành hai nhóm truy vấn chính:
1. **Log Stream Queries (Truy vấn luồng log)**: Trả về trực tiếp nội dung các dòng log, hỗ trợ lọc nhãn (stream selector) và lọc chuỗi (line filter expressions / regex).
2. **Metric Queries (Truy vấn chỉ số từ log)**: Áp dụng các hàm tổng hợp như `count_over_time`, `rate`, `bytes_over_time` để biến đổi log thành đồ thị chỉ số theo thời gian.

---

## 🔍 2. DANH SÁCH CÁC CÂU LỆNH TRUY VẤN MẪU (THEO YÊU CẦU ĐỀ BÀI)

### 🟢 Query 1: Lọc toàn bộ log của Nginx Reverse Proxy
- **Mục đích**: Xem toàn bộ dòng log truy cập (access log) và lỗi (error log) phát sinh qua Nginx.
- **Cú pháp LogQL**:
  ```logql
  {job="nginx"}
  ```
- **Giải thích**:
  - `{job="nginx"}`: Stream selector chọn tất cả các dòng log có nhãn `job` bằng `"nginx"` do Promtail thu thập từ `/var/log/nginx/*.log`.

---

### 🟡 Query 2: Lọc các yêu cầu HTTP gặp lỗi phía Client (4xx) hoặc Server (5xx)
- **Mục đích**: Phát hiện các lỗi truy cập trang web (ví dụ: 403 Forbidden do hardening chặn, 404 Not Found, 500 Internal Server Error, 502 Bad Gateway).
- **Cú pháp LogQL**:
  ```logql
  {job="nginx"} |~ " (4\\d{2}|5\\d{2}) "
  ```
- **Giải thích**:
  - `|~`: Toán tử Regex filter match.
  - `" (4\\d{2}|5\\d{2}) "`: Biểu thức chính quy tìm kiếm mã HTTP status code gồm 3 chữ số bắt đầu bằng số 4 hoặc số 5 có dấu cách bao quanh trong access log Nginx.

---

### 🔴 Query 3: Giám sát các nỗ lực truy cập trái phép hoặc tấn công bị Hardening chặn đứng (Security Alerts)
- **Mục đích**: Kiểm tra các hành vi dò quét file nhạy cảm (`.env`, `.git`), tấn công brute force WordPress qua `xmlrpc.php` hoặc truy cập thư mục uploads bị Nginx từ chối (403 Forbidden).
- **Cú pháp LogQL**:
  ```logql
  {job="nginx"} |= "403" or {job="nginx"} |= "xmlrpc.php"
  ```
- **Giải thích**:
  - `|=`: Toán tử line contains filter (tìm dòng chứa chuỗi).
  - Kết hợp logic `or` để gom các sự kiện mã 403 Forbidden và các request nhắm vào `xmlrpc.php`.

---

### 📊 Query 4: Tính toán tốc độ phát sinh lỗi HTTP 4xx/5xx theo thời gian (Metric Query)
- **Mục đích**: Vẽ biểu đồ đường trên Grafana thể hiện số lượng lỗi / giây để phát hiện các đợt tấn công hoặc sập dịch vụ.
- **Cú pháp LogQL**:
  ```logql
  sum(rate({job="nginx"} |~ " (4\\d{2}|5\\d{2}) " [5m]))
  ```
- **Giải thích**:
  - `[5m]`: Cửa sổ trượt (sliding window) tính toán trong 5 phút gần nhất.
  - `rate(...)`: Tính tốc độ số dòng log lỗi phát sinh trên mỗi giây.
  - `sum(...)`: Tổng hợp giá trị trên toàn bộ các luồng log.

---

### 🟣 Query 5: Lọc riêng các thông điệp cảnh báo và lỗi nghiêm trọng trong error.log
- **Mục đích**: Giúp Quản trị viên hệ thống (SysAdmin) điều tra sự cố Nginx không thể kết nối tới upstream backend hoặc lỗi cấu hình SSL.
- **Cú pháp LogQL**:
  ```logql
  {job="nginx", filename=~".*error.log"} |= "error" or {job="nginx", filename=~".*error.log"} |= "warn"
  ```
- **Giải thích**:
  - `filename=~".*error.log"`: Giới hạn tìm kiếm chỉ trong file `error.log`.
  - Lọc các dòng chứa mức nghiêm trọng `error` hoặc cảnh báo `warn`.

---

## 🛠️ 3. HƯỚNG DẪN THỰC THI TRÊN GRAFANA
1. Đăng nhập vào Grafana tại: `https://localhost/grafana/` hoặc `http://localhost:3000`.
2. Mở thanh menu bên trái, chọn **Explore** (biểu tượng la bàn).
3. Tại ô chọn nguồn dữ liệu (Datasource), chọn **Loki**.
4. Dán câu lệnh LogQL cần kiểm tra vào khung nhập query.
5. Nhấn **Run query** (hoặc tổ hợp phím `Shift + Enter`) để quan sát kết quả trực quan dạng Histogram và Log streams.
