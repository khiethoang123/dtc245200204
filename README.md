# BÀI TẬP LỚN: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM
## ĐỀ TÀI 3: WEBSITE QUẢNG BÁ SẢN PHẨM (WORDPRESS PRODUCTION STACK)

- **Họ và tên sinh viên**: Đặng Trần Hưng
- **Mã số sinh viên (MSSV)**: 20210001
- **Lớp**: CNTT - K15
- **Giảng viên hướng dẫn**: ThS. Giảng viên phụ trách môn học

---

## 📌 1. TỔNG QUAN HỆ THỐNG

Dự án triển khai một hệ thống website quảng bá sản phẩm hoàn chỉnh trên nền tảng **WordPress**, cơ sở dữ liệu **MySQL 8.0**, công cụ quản lý cơ sở dữ liệu **phpMyAdmin**, được đặt sau lớp bảo vệ của **Nginx Reverse Proxy** với kết nối an toàn **HTTPS (Self-signed SSL)** và các cấu hình **Hardening** chuyên sâu.

Hệ thống được thiết kế theo mô hình Container hóa chuẩn Docker Compose, phân tầng mạng cách ly (Network Isolation), tích hợp giám sát tài nguyên bằng **Prometheus & Grafana** và quản lý log tập trung bằng **Loki & Promtail**.

```
                   [ Internet / Client Browser ]
                                │
                                ▼ (Port 80 HTTP -> 301 Redirect HTTPS)
                                ▼ (Port 443 HTTPS - SSL / TLS 1.3)
                    ┌─────────────────────────┐
                    │   NGINX REVERSE PROXY   │ (Security Headers, Rate Limit, Hardening)
                    └───────────┬─────────────┘
                                │
       ┌────────────────────────┼────────────────────────┐
       │ (frontend-net)         │ (frontend-net)         │ (frontend-net)
       ▼                        ▼                        ▼
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│  WordPress   │         │  phpMyAdmin  │         │   Grafana    │
│  (Cổng 80)   │         │  (Cổng 80)   │         │ (Cổng 3000)  │
└──────┬───────┘         └──────┬───────┘         └──────────────┘
       │ (backend-net)          │ (backend-net)
       └───────────┬────────────┘
                   ▼
       ┌────────────────────────┐
       │     MySQL 8.0 DB       │ (Port 3306 KHÔNG public ra ngoài)
       └────────────────────────┘
```

---

## 🚀 2. HƯỚNG DẪN KHỞI CHẠY NHANH

### Bước 1: Sao chép file cấu hình môi trường
```bash
cp .env.example .env
```

### Bước 2: Tạo chứng chỉ SSL tự ký (nếu chưa có)
- Trên Linux / WSL:
```bash
chmod +x nginx/ssl/generate-cert.sh
./nginx/ssl/generate-cert.sh
```
- Trên Windows PowerShell:
```powershell
powershell -ExecutionPolicy Bypass -File .\nginx\ssl\generate-cert.ps1
```

### Bước 3: Khởi động hệ thống với Docker Compose
```bash
docker compose up -d
```

### Bước 4: Kiểm tra trạng thái các container
```bash
docker compose ps
```

---

## 🌐 3. CÁC ĐỊA CHỈ TRUY CẬP DỊCH VỤ

| Dịch vụ | Địa chỉ truy cập | Giao thức | Ghi chú |
| :--- | :--- | :--- | :--- |
| **Website WordPress** | [https://localhost](https://localhost) | HTTPS | Cổng 80 tự chuyển hướng sang 443 |
| **Quản trị phpMyAdmin** | [https://localhost/pma/](https://localhost/pma/) | HTTPS | Quản trị DB qua Nginx Reverse Proxy |
| **Giám sát Grafana** | [https://localhost/grafana/](https://localhost/grafana/) (hoặc `http://localhost:3000`) | HTTPS/HTTP | User: `admin` / Password trong `.env` |
| **Prometheus Metrics** | `http://localhost:9090` | HTTP | Bảng điều khiển thu thập chỉ số |
| **Loki Centralized Logs** | `http://localhost:3100` | HTTP | Dịch vụ lưu trữ và truy vấn LogQL |

---

## 🔒 4. CÁC BIỆN PHÁP HARDENING ĐÃ ÁP DỤNG

1. **Network Isolation (Phân tầng mạng cách ly)**:
   - `net_production_frontend`: Nginx giao tiếp với WordPress, phpMyAdmin và Grafana.
   - `net_production_backend`: Chỉ cho phép WordPress và phpMyAdmin kết nối đến MySQL. Port 3306 **tuyệt đối không mở ra ngoài Host**.
   - `net_production_monitoring`: Dành riêng cho Prometheus, Loki, Promtail và các Exporter.

2. **Nginx Security Hardening**:
   - Tự động chuyển hướng HTTP 301 sang HTTPS.
   - `server_tokens off;`: Ẩn hoàn toàn thông tin phiên bản Nginx.
   - Bổ sung toàn bộ Security Headers: `X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection`, `Strict-Transport-Security`, `Content-Security-Policy`, `Permissions-Policy`.
   - Chống tấn công brute force wp-login và DDoS với `limit_req_zone`.
   - Chặn đứng file nguy hiểm: Chặn thực thi PHP trong `wp-content/uploads`, chặn tấn công XML-RPC (`/xmlrpc.php`), chặn file ẩn (`.env`, `.git`).

3. **MySQL & Database Hardening**:
   - Vô hiệu hóa `local_infile=0` (ngăn chặn tấn công Arbitrary File Read).
   - Tắt `skip_symbolic_links`.
   - Cấp tài khoản riêng cho Prometheus exporter (`exporter`) tuân thủ nghiêm ngặt nguyên tắc đặc quyền tối thiểu (**Least Privilege**).

---

## 📝 5. LỊCH SỬ COMMITS THEO YÊU CẦU ĐỀ BÀI

- **Commit 1**: `feat(core): setup WordPress, MySQL 8.0, phpMyAdmin with hardened Nginx reverse proxy, SSL HTTPS & security headers`
- **Commit 2**: `feat(monitoring): integrate Prometheus, Grafana, cAdvisor, MySQL exporter and Nginx metrics with provisioned dashboards`
- **Commit 3**: `feat(logging): setup centralized logging with Loki and Promtail, including LogQL queries`
- **Commit 4**: `docs(report): add 10+ page comprehensive academic report, DOCX generator, and automation test scripts`
