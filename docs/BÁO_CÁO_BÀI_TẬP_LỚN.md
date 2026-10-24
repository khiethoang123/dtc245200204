# BỘ GIÁO DỤC VÀ ĐÀO TẠO
## TRƯỜNG ĐẠI HỌC CÔNG NGHỆ
### KHOA CÔNG NGHỆ THÔNG TIN - BỘ MÔN HỆ THỐNG THÔNG TIN VÀ MẠNG MÁY TÍNH

---

<br><br>

# BÁO CÁO BÀI TẬP LỚN
## MÔN HỌC: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM

<br>

### **ĐỀ TÀI 3:**
### **TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG WEBSITE QUẢNG BÁ SẢN PHẨM SỬ DỤNG WORDPRESS, CƠ SỞ DỮ LIỆU MYSQL, REVERSE PROXY NGINX, GIÁM SÁT PROMETHEUS - GRAFANA, QUẢN TRỊ LOG TẬP TRUNG LOKI VÀ BẢO MẬT GIA CỐ HỆ THỐNG (HARDENING)**

<br><br>

| Thông tin | Chi tiết |
| :--- | :--- |
| **Sinh viên thực hiện:** | **Đặng Trần Hưng** |
| **Mã số sinh viên (MSSV):** | **20210001** |
| **Lớp:** | **CNTT - K15** |
| **Chuyên ngành:** | Công nghệ Thông tin / Kỹ thuật Phần mềm |
| **Giảng viên hướng dẫn:** | ThS. Nguyễn Văn B |
| **Học kỳ / Năm học:** | Học kỳ I - Năm học 2026 - 2027 |

<br><br>

---
*Hà Nội, Tháng 10 Năm 2026*

\newpage

# LỜI CẢM ƠN

Trong suốt quá trình học tập và nghiên cứu môn học **Triển khai và Quản trị Hệ thống Phần mềm**, em đã có cơ hội tiếp cận với các kiến thức nền tảng và chuyên sâu về kiến trúc phần mềm hiện đại, công nghệ Container hóa (Containerization), điều phối dịch vụ với Docker Compose, kỹ thuật cân bằng tải và Reverse Proxy bằng Nginx, các giải pháp quan sát hệ thống (Observability) qua hệ thống Metrics (Prometheus + Grafana), hệ thống Log tập trung (Loki + Promtail), cũng như các phương pháp gia cố an ninh an toàn thông tin (System Hardening).

Em xin gửi lời cảm ơn chân thành và sâu sắc nhất tới Thầy/Cô phụ trách bộ môn đã tận tình truyền đạt kiến thức, hướng dẫn và giải đáp các vướng mắc kỹ thuật trong suốt thời gian qua. Những kiến thức thực tế quý báu này không chỉ giúp em hoàn thành tốt bài tập lớn này mà còn là hành trang vững chắc cho quá trình công tác chuyên môn sau khi tốt nghiệp.

Mặc dù em đã dành nhiều tâm huyết và nỗ lực để xây dựng hệ thống hoàn chỉnh theo đúng các tiêu chuẩn công nghiệp, song do thời gian và kinh nghiệm thực tế còn hạn chế nên bài báo cáo khó tránh khỏi những thiếu sót nhất định. Em rất mong nhận được những lời nhận xét, góp ý quý báu từ Thầy/Cô để hệ thống được hoàn thiện hơn nữa.

*Em xin chân thành cảm ơn!*

\newpage

# BẢNG NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN

| Tiêu chí đánh giá | Điểm tối đa | Điểm đánh giá | Ghi chú / Nhận xét |
| :--- | :---: | :---: | :--- |
| **1. Quản lý mã nguồn & Git commit** (Đúng quy chuẩn, commit rõ ràng, có README) | 1.5 | | |
| **2. Triển khai Web & Database** (WordPress, MySQL 8.0, phpMyAdmin hoạt động ổn định) | 2.0 | | |
| **3. Cấu hình Nginx Reverse Proxy** (HTTPS tự ký, Security Headers, Rate Limiting) | 1.5 | | |
| **4. Tích hợp Giám sát Prometheus + Grafana** (cAdvisor, MySQL, Nginx Exporter, Dashboards) | 1.5 | | |
| **5. Quản lý Log tập trung Loki + Promtail** (Cấu hình thu thập log, truy vấn LogQL) | 1.5 | | |
| **6. Kỹ thuật gia cố hệ thống (Hardening)** (Non-root, Network Isolation, Least Privilege) | 1.0 | | |
| **7. Chất lượng Báo cáo & Demo** (Cấu trúc tối thiểu 10 trang, phân tích sâu, minh họa rõ ràng) | 1.0 | | |
| **TỔNG ĐIỂM** | **10.0** | | |

<br><br>

**Ý kiến nhận xét chung:**  
.............................................................................................................................................................  
.............................................................................................................................................................  
.............................................................................................................................................................  
.............................................................................................................................................................  

<br>
*Hà Nội, ngày ...... tháng ...... năm 2026*  
**Giảng viên chấm điểm**  
*(Ký và ghi rõ họ tên)*  

\newpage

# MỤC LỤC

- [CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI VÀ MỤC TIÊU TRIỂN KHAI](#chương-1-tổng-quan-đề-tài-và-mục-tiêu-triển-khai)
  - [1.1. Bối cảnh và Tính cấp thiết của đề tài](#11-bối-cảnh-và-tính-cấp-thiết-của-đề-tài)
  - [1.2. Mục tiêu nghiên cứu và xây dựng hệ thống](#12-mục-tiêu-nghiên-cứu-và-xây-dựng-hệ-thống)
  - [1.3. Ngăn xếp công nghệ sử dụng (Technology Stack)](#13-ngăn-xếp-công-nghệ-sử-dụng-technology-stack)
  - [1.4. Yêu cầu chi tiết của bài toán](#14-yêu-cầu-chi-tiết-của-bài-toán)
- [CHƯƠNG 2: THIẾT KẾ KIẾN TRÚC HỆ THỐNG VÀ PHÂN TẦNG MẠNG](#chương-2-thiết-kế-kiến-trúc-hệ-thống-và-phân-tầng-mạng)
  - [2.1. Kiến trúc tổng thể hệ thống (High-Level Architecture)](#21-kiến-trúc-tổng-thể-hệ-thống-high-level-architecture)
  - [2.2. Phân tầng mạng cách ly (Network Isolation Design)](#22-phân-tầng-mạng-cách-ly-network-isolation-design)
  - [2.3. Thiết kế lưu trữ dữ liệu bền vững (Volume Persistence)](#23-thiết-kế-lưu-trữ-dữ-liệu-bền-vững-volume-persistence)
  - [2.4. Luồng xử lý dữ liệu và yêu cầu người dùng (Data Flow)](#24-luồng-xử-lý-dữ-liệu-và-yêu-cầu-người-dùng-data-flow)
- [CHƯƠNG 3: HIỆN THỰC ỨNG DỤNG WEB & NGINX REVERSE PROXY (COMMIT 1)](#chương-3-hiện-thực-ứng-dụng-web--nginx-reverse-proxy-commit-1)
  - [3.1. Triển khai dịch vụ WordPress Showcase](#31-triển-khai-dịch-vụ-wordpress-showcase)
  - [3.2. Cấu hình Cơ sở dữ liệu MySQL 8.0 & phpMyAdmin](#32-cấu-hình-cơ-sở-dữ-liệu-mysql-80--phpmyadmin)
  - [3.3. Cấu hình Nginx Reverse Proxy & Chuyển hướng HTTPS](#33-cấu-hình-nginx-reverse-proxy--chuyển-hướng-https)
  - [3.4. Khởi tạo Chứng chỉ SSL tự ký với SAN (Subject Alternative Name)](#34-khởi-tạo-chứng-chỉ-ssl-tự-ký-với-san-subject-alternative-name)
  - [3.5. Triển khai các Security Headers bảo vệ](#35-triển-khai-các-security-headers-bảo-vệ)
  - [3.6. Cơ chế giới hạn tốc độ (Rate Limiting) & Chặn truy cập nhạy cảm](#36-cơ-chế-giới-hạn-tốc-độ-rate-limiting--chặn-truy-cập-nhạy-cảm)
- [CHƯƠNG 4: HỆ THỐNG GIÁM SÁT TOÀN DIỆN VỚI PROMETHEUS & GRAFANA (COMMIT 2)](#chương-4-hệ-thống-giám-sát-toàn-diện-với-prometheus--grafana-commit-2)
  - [4.1. Kiến trúc hệ thống giám sát khả năng quan sát (Observability)](#41-kiến-trúc-hệ-thống-giám-sát-khả-năng-quan-sát-observability)
  - [4.2. Cấu hình Prometheus Server & Chiến lược Scrape Targets](#42-cấu-hình-prometheus-server--chiến-lược-scrape-targets)
  - [4.3. Giám sát Container với cAdvisor](#43-giám-sát-container-với-cadvisor)
  - [4.4. Giám sát Database với MySQL Exporter](#44-giám-sát-database-với-mysql-exporter)
  - [4.5. Giám sát Web Server với Nginx Prometheus Exporter](#45-giám-sát-web-server-với-nginx-prometheus-exporter)
  - [4.6. Tự động khởi tạo Dashboards & Datasources trên Grafana](#46-tự-động-khởi-tạo-dashboards--datasources-trên-grafana)
- [CHƯƠNG 5: HỆ THỐNG GHI LOG TẬP TRUNG LOKI & PROMTAIL (COMMIT 3)](#chương-5-hệ-thống-ghi-log-tập-trung-loki--promtail-commit-3)
  - [5.1. Thách thức trong quản lý Log và Giải pháp Grafana Loki](#51-thách-thức-trong-quản-lý-log-và-giải-pháp-grafana-loki)
  - [5.2. Cấu hình Promtail Agent thu thập nhật ký](#52-cấu-hình-promtail-agent-thu-thập-nhật-ký)
  - [5.3. Ngôn ngữ truy vấn LogQL và phân tích cú pháp](#53-ngôn-ngữ-truy-vấn-logql-và-phân-tích-cú-pháp)
  - [5.4. Hiện thực 5 câu truy vấn LogQL thực tế theo đề bài](#54-hiện-thực-5-câu-truy-vấn-logql-thực-tế-theo-đề-bài)
- [CHƯƠNG 6: CÁC BIỆN PHÁP GIA CỐ VÀ BẢO MẬT HỆ THỐNG (HARDENING)](#chương-6-các-biện-pháp-gia-cố-và-bảo-mật-hệ-thống-hardening)
  - [6.1. Vận hành Non-Root Containers](#61-vận-hành-non-root-containers)
  - [6.2. Network Isolation & Bảo vệ Cổng Database](#62-network-isolation--bảo-vệ-cổng-database)
  - [6.3. Nguyên tắc đặc quyền tối thiểu (Least Privilege)](#63-nguyên-tắc-đặc-quyền-tối-thiểu-least-privilege)
  - [6.4. Quản lý bí mật an toàn với .env](#64-quản-lý-bí-mật-an-toàn-với-env)
  - [6.5. Gia cố bảo mật Nginx và triệt tiêu lỗ hổng WordPress](#65-gia-cố-bảo-mật-nginx-và-triệt-tiêu-lỗ-hổng-wordpress)
- [CHƯƠNG 7: KỊCH BẢN KIỂM THỬ, ĐÁNH GIÁ VÀ HƯỚNG DẪN VẬN HÀNH](#chương-7-kịch-bản-kiểm-thử-đánh-giá-và-hướng-dẫn-vận-hành)
  - [7.1. Kịch bản kiểm thử chuyển hướng HTTPS và SSL](#71-kịch-bản-kiểm-thử-chuyển-hướng-https-và-ssl)
  - [7.2. Kịch bản kiểm thử Security Headers](#72-kịch-bản-kiểm-thử-security-headers)
  - [7.3. Kịch bản kiểm thử Hardening chặn XML-RPC và File nhạy cảm](#73-kịch-bản-kiểm-thử-hardening-chặn-xml-rpc-và-file-nhạy-cảm)
  - [7.4. Kịch bản kiểm thử truy vấn LogQL trên Grafana Explore](#74-kịch-bản-kiểm-thử-truy-vấn-logql-trên-grafana-explore)
  - [7.5. Hướng dẫn vận hành và bảo trì hệ thống](#75-hướng-dẫn-vận-hành-và-bảo-trì-hệ-thống)
- [CHƯƠNG 8: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN](#chương-8-kết-luận-và-hướng-phát-triển)
  - [8.1. Các kết quả đã hoàn thành](#81-các-kết-quả-đã-hoàn-thành)
  - [8.2. Hạn chế và Hướng mở rộng](#82-hạn-chế-và-hướng-mở-rộng)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)

\newpage

# DANH MỤC CÁC CHỮ VIẾT TẮT

| Viết tắt | Từ gốc tiếng Anh | Ý nghĩa chuyên môn |
| :--- | :--- | :--- |
| **API** | Application Programming Interface | Giao diện lập trình ứng dụng |
| **CSP** | Content Security Policy | Chính sách bảo mật nội dung trang web |
| **DBMS** | Database Management System | Hệ thống quản trị cơ sở dữ liệu |
| **DDoS** | Distributed Denial of Service | Tấn công từ chối dịch vụ phân tán |
| **HSTS** | HTTP Strict Transport Security | Cơ chế ép buộc sử dụng HTTPS an toàn |
| **HTTP** | Hypertext Transfer Protocol | Giao thức truyền tải siêu văn bản |
| **HTTPS** | Hypertext Transfer Protocol Secure | Giao thức truyền tải siêu văn bản an toàn có mã hóa |
| **MIME** | Multipurpose Internet Mail Extensions | Chuẩn định dạng kiểu dữ liệu trên Internet |
| **QPS** | Queries Per Second | Số lượng câu truy vấn trên mỗi giây |
| **RPS** | Requests Per Second | Số lượng yêu cầu HTTP trên mỗi giây |
| **SAN** | Subject Alternative Name | Phần mở rộng tên miền bổ sung trong chứng chỉ số X.509 |
| **SSL** | Secure Sockets Layer | Giao thức bảo mật lớp truyền tải |
| **TLS** | Transport Layer Security | Giao thức bảo mật lớp truyền tải hiện đại |
| **UID/GID**| User Identifier / Group Identifier | Mã định danh người dùng và nhóm trong Linux |
| **URI** | Uniform Resource Identifier | Định danh tài nguyên đồng nhất |
| **URL** | Uniform Resource Locator | Địa chỉ tài nguyên đồng nhất |
| **XSS** | Cross-Site Scripting | Lỗ hổng chèn mã độc kịch bản liên trang web |

\newpage

# CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI VÀ MỤC TIÊU TRIỂN KHAI

## 1.1. Bối cảnh và Tính cấp thiết của đề tài
Trong kỷ nguyên số hóa hiện đại, các ứng dụng web thương mại điện tử và website quảng bá sản phẩm đóng vai trò là cửa ngõ giao tiếp trực tiếp giữa doanh nghiệp và khách hàng. Một hệ thống website thành công trong môi trường thực tế (Production) không chỉ đòi hỏi giao diện thân thiện và tính năng phong phú, mà quan trọng hơn hết là phải đảm bảo các tiêu chuẩn khắt khe về **tính sẵn sàng cao (High Availability)**, **khả năng chịu tải linh hoạt (Scalability)**, **tính an toàn thông tin (Security)** và **khả năng giám sát toàn diện (Observability)**.

Trước đây, các hệ thống web truyền thống thường được cài đặt trực tiếp trên hệ điều hành máy chủ vật lý theo mô hình nguyên khối (Monolithic bare-metal). Cách tiếp cận này bộc lộ rất nhiều hạn chế:
- **Xung đột môi trường**: Xung đột phiên bản thư viện giữa các phần mềm cùng chạy trên một hệ điều hành.
- **Khó khăn trong đóng gói và mở rộng**: Việc sao chép hoặc di chuyển môi trường triển khai tốn nhiều thời gian và dễ phát sinh lỗi con người.
- **Thiếu cô lập bảo mật**: Một lỗ hổng bảo mật trên ứng dụng web có thể cho phép kẻ tấn công leo thang đặc quyền và kiểm soát toàn bộ cơ sở dữ liệu cùng máy chủ host.
- **Mù mờ thông tin vận hành**: Quản trị viên chỉ biết hệ thống gặp sự cố khi người dùng phàn nàn, do thiếu cơ chế cảnh báo chỉ số và nhật ký tập trung.

Để giải quyết triệt để các vấn đề trên, đề tài này tiến hành nghiên cứu và triển khai giải pháp kiến trúc hệ thống hiện đại dựa trên công nghệ Container hóa của Docker và Docker Compose, kết hợp lớp bảo vệ Reverse Proxy của Nginx, hệ thống giám sát Metrics thời gian thực (Prometheus + Grafana), hệ thống thu thập phân tích Log tập trung (Loki + Promtail) và các giải pháp gia cố bảo mật chuyên sâu (Hardening).

## 1.2. Mục tiêu nghiên cứu và xây dựng hệ thống
Đề tài hướng tới các mục tiêu cụ thể sau:
1. **Container hóa toàn diện**: Đóng gói toàn bộ các dịch vụ (Website, Database, Reverse Proxy, Exporters, Monitoring, Logging) thành các container độc lập, vận hành đồng bộ thông qua tệp khai báo điều phối `docker-compose.yml`.
2. **Xây dựng lớp bảo vệ Reverse Proxy an toàn**: Ứng dụng Nginx đóng vai trò Reverse Proxy duy nhất tiếp nhận lưu lượng từ người dùng, thực thi chuyển hướng HTTP 301 sang HTTPS với chứng chỉ SSL tự ký có Subject Alternative Name (SAN), áp dụng bộ quy tắc Security Headers chống tấn công XSS, Clickjacking, MIME-sniffing, và cơ chế giới hạn tốc độ (Rate Limiting).
3. **Phân tầng mạng cách ly (Network Isolation)**: Thiết kế 3 lớp mạng ảo biệt lập (`frontend-net`, `backend-net`, `monitoring-net`), đảm bảo cổng cơ sở dữ liệu MySQL 3306 hoàn toàn bị khóa với môi trường bên ngoài và chỉ phục vụ nội bộ.
4. **Giám sát hiệu năng và tài nguyên đa tầng**: Thu thập chỉ số tài nguyên phần cứng, trạng thái container qua cAdvisor, thống kê lưu lượng Nginx qua Nginx Exporter, và đo lường truy vấn Database qua MySQL Exporter; tự động trực quan hóa thông qua các bảng điều khiển (Dashboards) trên Grafana.
5. **Quản trị nhật ký tập trung (Centralized Logging)**: Triển khai Loki và Promtail để thu thập access log và error log, cung cấp ngôn ngữ truy vấn LogQL giúp điều tra sự cố và phát hiện tấn công trong thời gian thực.
6. **Thực thi nguyên tắc gia cố bảo mật (System Hardening)**: Áp dụng người dùng không đặc quyền (Non-root user), nguyên tắc đặc quyền tối thiểu (Least Privilege), quản lý biến môi trường bảo mật, và vô hiệu hóa các tính năng nguy hiểm của WordPress và MySQL.

## 1.3. Ngăn xếp công nghệ sử dụng (Technology Stack)
Dự án được xây dựng dựa trên ngăn xếp công nghệ tiêu chuẩn công nghiệp:

| Thành phần | Công nghệ / Hình ảnh | Phiên bản | Vai trò trong hệ thống |
| :--- | :--- | :--- | :--- |
| **Web Server / Reverse Proxy** | `nginx:1.27-alpine` | 1.27 | Điểm tiếp nhận truy cập, SSL Termination, Security Headers, Rate Limiting |
| **Web Application** | `wordpress:6.7-apache`| 6.7 | Nền tảng website quảng bá sản phẩm, quản lý danh mục và bài viết |
| **Database Server** | `mysql:8.0` | 8.0 | Hệ quản trị cơ sở dữ liệu quan hệ lưu trữ thông tin sản phẩm và cấu hình |
| **Database GUI Management** | `phpmyadmin:5.2-apache` | 5.2 | Giao diện trực quan quản lý cơ sở dữ liệu qua giao duyệt web |
| **Time-series Database** | `prom/prometheus:v2.50.1` | 2.50.1 | Thu thập và lưu trữ các chuỗi số liệu thời gian thực (Metrics) |
| **Visualization Platform** | `grafana/grafana:10.4.0` | 10.4.0 | Trực quan hóa dữ liệu chỉ số và nhật ký qua các Dashboard tùy biến |
| **Container Metrics Exporter**| `gcr.io/cadvisor/cadvisor:v0.49.1` | 0.49.1 | Thu thập số liệu CPU, RAM, Network, Disk I/O của toàn bộ Containers |
| **MySQL Metrics Exporter** | `prom/mysqld-exporter:v0.15.1` | 0.15.1 | Thu thập số liệu QPS, Uptime, Buffer pool, Threads của MySQL |
| **Nginx Metrics Exporter** | `nginx/nginx-prometheus-exporter:1.1.0` | 1.1.0 | Thu thập số liệu RPS, Active connections qua endpoint `/stub_status` |
| **Node Metrics Exporter** | `prom/node-exporter:v1.7.0` | 1.7.0 | Giám sát tài nguyên phần cứng hệ điều hành máy chủ host |
| **Log Aggregator** | `grafana/loki:2.9.4` | 2.9.4 | Hệ thống lưu trữ và đánh chỉ mục nhật ký tập trung |
| **Log Shipper / Agent** | `grafana/promtail:2.9.4` | 2.9.4 | Đọc tệp log Nginx, gắn nhãn metadata và đẩy về Loki |
| **Orchestration Tool** | `docker compose` | v2.x | Quản lý vòng đời và cấu hình liên kết toàn bộ container |

## 1.4. Yêu cầu chi tiết của bài toán
Dự án phải đáp ứng đầy đủ 7 nhóm yêu cầu kỹ thuật do đề bài quy định:
- **Yêu cầu 1**: Quản lý toàn bộ mã nguồn trên Git với lịch sử commit rõ ràng, có tài liệu hướng dẫn README chi tiết.
- **Yêu cầu 2**: Triển khai website WordPress với Database MySQL và công cụ quản trị phpMyAdmin.
- **Yêu cầu 3**: Cấu hình Nginx làm Reverse Proxy, hỗ trợ HTTPS tự ký và bảo mật Security Headers -> Tương ứng **Commit 1**.
- **Yêu cầu 4**: Tích hợp Prometheus + Grafana giám sát container, web server và database -> Tương ứng **Commit 2**.
- **Yêu cầu 5**: Triển khai hệ thống log tập trung Loki + Promtail, truy vấn log bằng LogQL ít nhất 2 - 3 câu truy vấn -> Tương ứng **Commit 3**.
- **Yêu cầu 6**: Thực thi các biện pháp Hardening toàn diện (non-root container, network isolation, mật khẩu mạnh, hạn chế quyền, Nginx security headers).
- **Yêu cầu 7**: Lập báo cáo khoa học tổng hợp tối thiểu 10 trang, trình bày trang bìa chuẩn báo cáo thực tập, cấu trúc hệ thống, nguyên lý vận hành và kết quả kiểm thử.

\newpage

# CHƯƠNG 2: THIẾT KẾ KIẾN TRÚC HỆ THỐNG VÀ PHÂN TẦNG MẠNG

## 2.1. Kiến trúc tổng thể hệ thống (High-Level Architecture)
Hệ thống được thiết kế theo mô hình kiến trúc phân tầng dạng Micro-services và Observability Stack. Mọi lưu lượng từ mạng bên ngoài đều được chặn ở biên giới và buộc phải đi qua Nginx Reverse Proxy. Không một dịch vụ phụ trợ nào (MySQL, Exporters, Loki) được phép mở cổng công khai ra Internet mà không qua kiểm soát.

```
                              [ Client / Web Browser ]
                                          │
                                          ▼
                               [ Cổng 80: HTTP Redirect ]
                               [ Cổng 443: HTTPS / TLS 1.3 ]
                       ┌──────────────────────────────────────┐
                       │     NGINX REVERSE PROXY & HARDENING  │
                       │  - SSL Termination (Self-signed SAN) │
                       │  - Security Headers & Rate Limiting  │
                       │  - Sensitive Path Blocking           │
                       └──────────────────┬───────────────────┘
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         │                                │                                │
 (net_production_frontend)        (net_production_frontend)        (net_production_frontend)
         ▼                                ▼                                ▼
┌─────────────────┐              ┌─────────────────┐              ┌─────────────────┐
│   WordPress     │              │   phpMyAdmin    │              │     Grafana     │
│ (Showcase Web)  │              │ (Database GUI)  │              │ (Visual Portal) │
│    Cổng 80      │              │    Cổng 80      │              │    Cổng 3000    │
└────────┬────────┘              └────────┬────────┘              └────────┬────────┘
         │                                │                                │
         └────────────────┬───────────────┘                                │
                          │ (net_production_backend)                       │
                          ▼                                                │
                 ┌─────────────────┐                                       │
                 │    MySQL 8.0    │                                       │
                 │ (Internal Only) │                                       │
                 │    Cổng 3306    │                                       │
                 └────────▲────────┘                                       │
                          │                                                │
         ┌────────────────┴────────────────┐                               │
         │ (net_production_backend)        │                               │
         ▼                                 │                               │
┌─────────────────┐                        │                               │
│  MySQL Exporter │                        │                               │
│   (Port 9104)   │                        │                               │
└────────┬────────┘                        │                               │
         │                                 │                               │
         │ (net_production_monitoring)     │                               │
         ▼                                 ▼                               ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                           OBSERVABILITY & LOGGING STACK                           │
│  ┌──────────────────────┐  ┌──────────────────────┐  ┌─────────────────────────┐  │
│  │   Prometheus 2.50    │  │     cAdvisor 0.49    │  │      Nginx Exporter     │  │
│  │     (Port 9090)      │  │      (Port 8080)     │  │        (Port 9113)      │  │
│  └──────────┬───────────┘  └──────────────────────┘  └─────────────────────────┘  │
│             │                                                                     │
│             │                  ┌──────────────────────┐  ┌─────────────────────┐  │
│             └─────────────────►│      Loki 2.9        │◄─┤    Promtail 2.9     │  │
│                                │     (Port 3100)      │  │ (Scrapes Nginx Logs)│  │
│                                └──────────────────────┘  └─────────────────────┘  │
└───────────────────────────────────────────────────────────────────────────────────┘
```

## 2.2. Phân tầng mạng cách ly (Network Isolation Design)
Một trong những lỗ hổng phổ biến nhất trong triển khai Docker nghiệp dư là sử dụng mạng mặc định (`bridge` default) khiến mọi container có thể tự do thăm dò và kết nối chéo với nhau. Để triệt tiêu hoàn toàn rủi ro này, dự án thiết kế **3 mạng ảo riêng biệt (Isolated Docker Networks)**:

1. **Mạng Tiền sảnh (`net_production_frontend`)**:
   - **Mục đích**: Kết nối Nginx Reverse Proxy với các giao diện người dùng bao gồm WordPress, phpMyAdmin và Grafana.
   - **Các container tham gia**: `production-nginx`, `production-wordpress`, `production-phpmyadmin`, `production-grafana`, `production-nginx-exporter`, `production-prometheus`.
   - **Cơ chế an toàn**: Người dùng bên ngoài chỉ tương tác với Nginx, Nginx định tuyến gói tin đến container đích thông qua DNS nội bộ của Docker.

2. **Mạng Hậu sảnh Cơ sở dữ liệu (`net_production_backend`)**:
   - **Mục đích**: Lưu chuyển dữ liệu nhạy cảm giữa ứng dụng và máy chủ cơ sở dữ liệu.
   - **Các container tham gia**: `production-wordpress`, `production-phpmyadmin`, `production-mysql`, `production-mysql-exporter`.
   - **Cơ chế an toàn**: Nginx và máy chủ bên ngoài **HOÀN TOÀN KHÔNG THỂ** kết nối trực tiếp vào MySQL. Cổng 3306 chỉ mở trên giao diện ảo của mạng này.

3. **Mạng Giám sát và Nhật ký (`net_production_monitoring`)**:
   - **Mục đích**: Thu thập và truyền tải dữ liệu đo đạc (Metrics) và dòng nhật ký (Logs).
   - **Các container tham gia**: `production-prometheus`, `production-grafana`, `production-cadvisor`, `production-mysql-exporter`, `production-nginx-exporter`, `production-node-exporter`, `production-loki`, `production-promtail`, `production-nginx`.
   - **Cơ chế an toàn**: Cô lập dữ liệu vận hành khỏi luồng truy cập của khách hàng, đảm bảo khi ứng dụng bị nghẽn mạng thì hệ thống giám sát vẫn hoạt động ổn định.

## 2.3. Thiết kế lưu trữ dữ liệu bền vững (Volume Persistence)
Khi container bị khởi động lại, nâng cấp hoặc xóa bỏ, dữ liệu bên trong container sẽ bị mất nếu không được cấu hình lưu trữ bền vững. Dự án khai báo các Docker Named Volumes độc lập:

| Tên Volume | Đường dẫn Mount trên Container | Mục đích lưu trữ |
| :--- | :--- | :--- |
| `vol_production_mysql_data` | `/var/lib/mysql` | Lưu trữ toàn bộ bảng dữ liệu, chỉ mục và nhật ký nhị phân của MySQL 8.0 |
| `vol_production_wordpress_data`| `/var/www/html` | Lưu trữ mã nguồn, thư viện plugin, theme và hình ảnh sản phẩm upload |
| `vol_production_nginx_logs` | `/var/log/nginx` | Chia sẻ tệp `access.log` và `error.log` từ Nginx sang Promtail |
| `vol_production_prometheus_data`| `/prometheus` | Lưu trữ cơ sở dữ liệu chuỗi thời gian (TSDB) của Prometheus trong 15 ngày |
| `vol_production_grafana_data` | `/var/lib/grafana` | Lưu trữ tài khoản người dùng, phiên làm việc và cấu hình Grafana |
| `vol_production_loki_data` | `/loki` | Lưu trữ các khối dữ liệu nhật ký nén (Chunks) và chỉ mục TSDB của Loki |

## 2.4. Luồng xử lý dữ liệu và yêu cầu người dùng (Data Flow)
Quy trình xử lý một yêu cầu duyệt sản phẩm diễn ra theo các bước nghiêm ngặt:
1. **Tiếp nhận & Ép buộc HTTPS**: Trình duyệt gửi request tới cổng 80 (`http://localhost`). Nginx phản hồi ngay lập tức mã `301 Moved Permanently` điều hướng sang cổng 443 (`https://localhost`).
2. **Kiểm tra SSL & Lọc bảo mật**: Nginx thực hiện bắt tay mã hóa TLSv1.3 với client. Sau đó, request được chuyển qua bộ lọc kiểm tra:
   - Nếu truy cập `/xmlrpc.php` hoặc file có đuôi `.php` trong thư mục `uploads` -> Nginx trả về `403 Forbidden` ngay tại tầng proxy.
   - Nếu tần suất request vượt ngưỡng quy định (`rate=20r/s`) -> Kích hoạt giới hạn tốc độ.
3. **Chuyển tiếp Upstream**: Nginx bổ sung các tiêu đề nhận diện máy khách (`X-Real-IP`, `X-Forwarded-For`, `X-Forwarded-Proto`) và chuyển tiếp gói tin qua mạng `frontend-net` tới `http://wordpress:80`.
4. **Truy vấn Cơ sở dữ liệu**: WordPress tiếp nhận yêu cầu, thực thi mã nguồn PHP và gửi truy vấn SQL tới `mysql:3306` qua mạng nội bộ `backend-net`.
5. **Phản hồi & Đính kèm Security Headers**: Nginx nhận lại trang HTML từ WordPress, tự động chèn thêm toàn bộ các tiêu đề bảo mật (`X-Frame-Options`, `Content-Security-Policy`,...) và gửi trả về trình duyệt của khách hàng.
6. **Thu thập Metrics & Logs**: Đồng thời, Nginx ghi lại nhật ký request vào tệp `access.log`. Promtail ngay lập tức đọc dòng log này và đẩy về Loki. Nginx Exporter tăng bộ đếm `nginx_http_requests_total` để Prometheus kéo về theo chu kỳ.

\newpage

# CHƯƠNG 3: HIỆN THỰC ỨNG DỤNG WEB & NGINX REVERSE PROXY (COMMIT 1)

## 3.1. Triển khai dịch vụ WordPress Showcase
Ứng dụng web được triển khai bằng hình ảnh chính thức `wordpress:6.7-apache`. Để phục vụ mục đích quảng bá sản phẩm chuyên nghiệp, hệ thống được cấu hình:
- **Tối ưu hóa môi trường PHP**: Tệp cấu hình `wordpress/uploads.ini` được mount vào thư mục cấu hình PHP của container, nâng giới hạn kích thước tệp tải lên lên `64M`, dung lượng bộ nhớ `256M`, tắt `expose_php = Off` để không lộ phiên bản PHP.
- **Tích hợp phía sau Reverse Proxy**: Thông qua biến môi trường `WORDPRESS_CONFIG_EXTRA`, mã nguồn WordPress tự động nhận diện tiêu đề `HTTP_X_FORWARDED_PROTO` do Nginx gửi sang. Khi phát hiện giá trị `https`, WordPress tự động gán cờ `$_SERVER['HTTPS'] = 'on'`, đảm bảo toàn bộ đường link CSS, Javascript và hình ảnh tải về đều sử dụng giao thức HTTPS, loại bỏ hoàn toàn lỗi **Mixed Content** thường gặp.

## 3.2. Cấu hình Cơ sở dữ liệu MySQL 8.0 & phpMyAdmin
Dịch vụ cơ sở dữ liệu sử dụng hình ảnh chính thức `mysql:8.0`. Để phục vụ đồng thời tính ổn định và tính bảo mật cao, cấu hình bao gồm:
- **Tối ưu hóa hiệu năng**: Cấu hình bộ nhớ đệm `innodb_buffer_pool_size=256M` phù hợp với khối lượng dữ liệu sản phẩm vừa và lớn; `innodb_flush_log_at_trx_commit=2` tăng tốc độ ghi dữ liệu.
- **Khởi tạo dữ liệu tự động**: Tệp script SQL `mysql/init/01-init.sql` được đặt trong thư mục `/docker-entrypoint-initdb.d/`. Khi container khởi tạo lần đầu, hệ thống sẽ tự động tạo cơ sở dữ liệu `wordpress_db` với bảng mã `utf8mb4_unicode_ci` chuẩn tiếng Việt.
- **Công cụ phpMyAdmin**: Sử dụng hình ảnh `phpmyadmin:5.2-apache`, được kết nối nội bộ tới máy chủ `mysql` qua biến `PMA_HOST: mysql`. Đồng thời thiết lập `PMA_ABSOLUTE_URI: https://localhost/pma/` để phpMyAdmin có thể hoạt động hoàn hảo dưới tiền tố đường dẫn `/pma/` của Nginx Reverse Proxy.

## 3.3. Cấu hình Nginx Reverse Proxy & Chuyển hướng HTTPS
Nginx đóng vai trò là "người gác cổng" duy nhất cho toàn bộ hệ thống. Tệp cấu hình `nginx/conf.d/default.conf` được chia làm hai khối máy chủ (Server Blocks):
1. **Khối Server HTTP (Cổng 80)**:
   ```nginx
   server {
       listen 80;
       server_name localhost _;
       server_tokens off;
       location / {
           return 301 https://$host$request_uri;
       }
   }
   ```
   Mọi truy cập không an toàn đều bị chuyển hướng vĩnh viễn (HTTP 301) sang cổng 443 với giao thức HTTPS.

2. **Khối Server HTTPS (Cổng 443)**:
   - Kích hoạt HTTP/2 (`http2 on;`) giúp tăng tốc độ truyền tải trang web bằng kỹ thuật dồn kênh (Multiplexing).
   - Thiết lập bộ mã hóa an toàn cao: Chỉ cho phép TLSv1.2 và TLSv1.3, vô hiệu hóa các giao thức lỗi thời và kém an toàn như SSLv3, TLS 1.0, TLS 1.1.

## 3.4. Khởi tạo Chứng chỉ SSL tự ký với SAN (Subject Alternative Name)
Trình duyệt web hiện đại (Google Chrome, Microsoft Edge, Mozilla Firefox) từ chối các chứng chỉ SSL chỉ khai báo `Common Name (CN)` đơn thuần. Do đó, chứng chỉ tự ký của dự án được tạo với phần mở rộng **Subject Alternative Name (SAN)** qua tệp cấu hình OpenSSL:
```ini
[alt_names]
DNS.1 = localhost
DNS.2 = *.localhost
DNS.3 = wp.local
DNS.4 = pma.local
IP.1 = 127.0.0.1
IP.2 = ::1
```
Script tự động hóa `nginx/ssl/generate-cert.ps1` và `nginx/ssl/generate-cert.sh` sử dụng thuật toán mã hóa khóa công khai RSA 2048-bit và hàm băm SHA-256 để phát hành cặp khóa `selfsigned.crt` và `selfsigned.key` với thời hạn 365 ngày.

## 3.5. Triển khai các Security Headers bảo vệ
Tệp cấu hình `nginx/security-headers.conf` được nhúng vào khối máy chủ HTTPS, cung cấp một lá chắn phòng thủ chiều sâu:
- **`X-Frame-Options: SAMEORIGIN`**: Chống tấn công Clickjacking bằng cách ngăn các trang web bên thứ ba nhúng website vào trong thẻ `<iframe>`.
- **`X-Content-Type-Options: nosniff`**: Buộc trình duyệt tuân thủ chặt chẽ MIME type do server gửi về, ngăn chặn tấn công chèn mã độc ngụy trang dưới dạng ảnh.
- **`X-XSS-Protection: 1; mode=block`**: Kích hoạt bộ lọc chống Cross-Site Scripting tích hợp sẵn của trình duyệt.
- **`Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`**: Cơ chế HSTS buộc trình duyệt chỉ kết nối bằng HTTPS trong vòng 1 năm.
- **`Referrer-Policy: strict-origin-when-cross-origin`**: Bảo vệ tính riêng tư của đường dẫn URL khi người dùng chuyển hướng ra website ngoài.
- **`Content-Security-Policy (CSP)`**: Giới hạn nguồn gốc tải tài nguyên script, stylesheet, hình ảnh, ngăn ngừa thực thi mã độc tùy ý.
- **`Permissions-Policy`**: Khóa các API phần cứng không cần thiết như vị trí (Geolocation), máy ảnh (Camera) và micrô (Microphone).

## 3.6. Cơ chế giới hạn tốc độ (Rate Limiting) & Chặn truy cập nhạy cảm
Để bảo vệ ứng dụng trước các đợt tấn công từ chối dịch vụ (DoS) và dò quét tự động:
- **Rate Limiting tổng thể**: Khai báo vùng nhớ `general_limit` giới hạn tối đa 20 request/giây cho mỗi địa chỉ IP nguồn.
- **Rate Limiting trang đăng nhập**: Vùng nhớ `login_limit` giới hạn riêng cho URL `/wp-login.php` ở mức tối đa 3 request/giây với kích thước bùng nổ `burst=5`. Mọi nỗ lực brute force mật khẩu quản trị đều bị bóp nghẽn và trả về mã lỗi `503 Service Temporarily Unavailable`.
- **Chặn đứng lỗ hổng XML-RPC**: WordPress thường xuyên bị tấn công qua endpoint `/xmlrpc.php`. Nginx chặn tuyệt đối tệp này với chỉ thị `deny all;`.
- **Chặn thực thi PHP trong thư mục tải lên**: Hacker thường tìm cách upload webshell vào thư mục `wp-content/uploads/`. Nginx thiết lập quy tắc `location ~* /wp-content/uploads/.*\.php$ { deny all; }` ngăn chặn triệt để hành vi này.

\newpage

# CHƯƠNG 4: HỆ THỐNG GIÁM SÁT TOÀN DIỆN VỚI PROMETHEUS & GRAFANA (COMMIT 2)

## 4.1. Kiến trúc hệ thống giám sát khả năng quan sát (Observability)
Khả năng quan sát là yếu tố sống còn của một hệ thống Production. Hệ thống giám sát của dự án bao gồm 3 tầng:
1. **Tầng Thu thập (Data Collection - Exporters)**: Các chương trình Exporter đọc dữ liệu từ nhân hệ điều hành, cờ thống kê của MySQL và máy chủ web Nginx, sau đó chuyển đổi thành định dạng số liệu chuẩn Prometheus.
2. **Tầng Lưu trữ (Time-Series Storage - Prometheus)**: Prometheus định kỳ gửi HTTP GET (Scrape) tới các exporter để thu thập mẫu số liệu và ghi vào cơ sở dữ liệu chuỗi thời gian (TSDB).
3. **Tầng Trực quan hóa (Data Visualization - Grafana)**: Grafana kết nối vào Prometheus thông qua ngôn ngữ truy vấn PromQL và hiển thị các đồ thị trực quan, hỗ trợ thiết lập ngưỡng cảnh báo (Alerting).

## 4.2. Cấu hình Prometheus Server & Chiến lược Scrape Targets
Tệp cấu hình `monitoring/prometheus/prometheus.yml` định nghĩa 5 công việc thu thập dữ liệu (Scrape Jobs):
- `job_name: 'prometheus'`: Tự giám sát tình trạng bộ nhớ và thời gian tính toán truy vấn của chính Prometheus (chu kỳ 15s).
- `job_name: 'cadvisor'`: Thu thập toàn bộ chỉ số tài nguyên phần cứng của tất cả các container trong hệ thống (chu kỳ 10s).
- `job_name: 'nginx'`: Thu thập số liệu thống kê máy chủ Nginx từ `nginx-exporter:9113` (chu kỳ 10s).
- `job_name: 'mysql'`: Thu thập số liệu hiệu năng cơ sở dữ liệu từ `mysql-exporter:9104` (chu kỳ 10s).
- `job_name: 'node-exporter'`: Thu thập tải CPU, RAM, dung lượng ổ cứng của máy chủ host (chu kỳ 15s).

Prometheus được cấu hình thời gian lưu trữ dữ liệu là 15 ngày (`--storage.tsdb.retention.time=15d`) và vận hành dưới người dùng không đặc quyền `user: nobody`.

## 4.3. Giám sát Container với cAdvisor
`cAdvisor (Container Advisor)` là công cụ mã nguồn mở của Google chuyên biệt cho việc phân tích mức độ tiêu thụ tài nguyên và đặc tính hiệu năng của các container đang chạy. cAdvisor được mount trực tiếp tới hệ thống tệp gốc của máy chủ (`/sys`, `/var/run/docker.sock`, `/var/lib/docker`) để đọc các thông số từ Linux Control Groups (cgroups):
- Tỷ lệ phần trăm CPU tiêu thụ theo từng container: `container_cpu_usage_seconds_total`.
- Dung lượng bộ nhớ RAM chiếm dụng thực tế: `container_memory_usage_bytes`.
- Băng thông mạng vào/ra (RX/TX Network Throughput): `container_network_receive_bytes_total`.
- Tần suất đọc ghi đĩa cứng (Disk I/O operations).

## 4.4. Giám sát Database với MySQL Exporter
`MySQL Exporter (mysqld_exporter)` kết nối tới cơ sở dữ liệu MySQL bằng tài khoản phân quyền tối thiểu `exporter` đã được khởi tạo trong `01-init.sql`. Exporter cung cấp các chỉ số quan trọng:
- `mysql_global_status_uptime`: Thời gian dịch vụ MySQL hoạt động liên tục (tính bằng giây).
- `mysql_global_status_threads_connected`: Số lượng kết nối client hiện thời đang mở.
- `mysql_global_status_queries`: Tổng số lượng truy vấn SQL đã xử lý, giúp tính toán QPS (Queries Per Second) theo thời gian thực: `rate(mysql_global_status_queries[1m])`.
- Băng thông mạng cơ sở dữ liệu: `mysql_global_status_bytes_received` và `bytes_sent`.

## 4.5. Giám sát Web Server với Nginx Prometheus Exporter
Nginx Exporter đọc số liệu từ cổng nội bộ `http://nginx:8080/stub_status` do module `http_stub_status_module` cung cấp:
- `nginx_http_requests_total`: Tổng số lượt yêu cầu HTTP đã phục vụ, từ đó tính toán được RPS (Requests Per Second): `rate(nginx_http_requests_total[1m])`.
- `nginx_connections_active`: Số lượng kết nối đang mở đồng thời.
- `nginx_connections_reading`, `writing`, `waiting`: Phân loại trạng thái kết nối giúp phát hiện tắc nghẽn ở tầng mạng hoặc tầng xử lý PHP.

## 4.6. Tự động khởi tạo Dashboards & Datasources trên Grafana
Để loại bỏ hoàn toàn thao tác cấu hình thủ công bằng tay sau khi triển khai, dự án áp dụng kỹ thuật **Grafana Provisioning**:
- **Tự động đăng ký Datasource**: Tệp `monitoring/grafana/provisioning/datasources/datasources.yml` tự động thiết lập kết nối tới `http://prometheus:9090` làm nguồn dữ liệu mặc định.
- **Tự động nạp Dashboards**: Tệp `monitoring/grafana/provisioning/dashboards/dashboards.yml` chỉ định Grafana tự động quét và nạp toàn bộ các tệp JSON trong thư mục `/etc/grafana/provisioning/dashboards/json`:
  1. `docker-containers.json`: Dashboard giám sát tổng thể CPU, RAM, Network của từng container.
  2. `nginx-overview.json`: Dashboard theo dõi lưu lượng truy cập web, RPS, số kết nối đang xử lý.
  3. `mysql-overview.json`: Dashboard theo dõi hiệu năng database, số lượng truy vấn QPS, kết nối đồng thời.

\newpage

# CHƯƠNG 5: HỆ THỐNG GHI LOG TẬP TRUNG LOKI & PROMTAIL (COMMIT 3)

## 5.1. Thách thức trong quản lý Log và Giải pháp Grafana Loki
Trong môi trường micro-services gồm nhiều container phân tán, việc điều tra sự cố gặp nhiều trở ngại lớn:
- Nhật ký bị phân mảnh nằm rải rác bên trong từng container riêng lẻ.
- Khi một container bị xóa bỏ hoặc gặp lỗi sập (crash), toàn bộ dữ liệu log chưa kịp lưu sẽ biến mất hoàn toàn.
- Lệnh `docker logs` truyền thống không hỗ trợ lọc nâng cao theo thời gian, phân tích chuỗi phức tạp hoặc vẽ biểu đồ cảnh báo.

Giải pháp **Grafana Loki** được mệnh danh là "Prometheus dành cho Logs". Khác với Elasticsearch tốn kém dung lượng do đánh chỉ mục toàn văn bản (Full-text indexing), Loki chỉ lập chỉ mục cho các nhãn siêu dữ liệu (Labels) giống như Prometheus, trong khi nội dung thông điệp log được nén thành các khối (Chunks) lưu trữ trên hệ thống tệp. Kiến trúc này giúp Loki cực kỳ nhẹ, tiết kiệm RAM và tốc độ truy vấn vượt trội.

## 5.2. Cấu hình Promtail Agent thu thập nhật ký
`Promtail` đóng vai trò là log shipper (agent thu thập log) chạy ngầm trong hệ sinh thái:
- Promtail mount volume chung `nginx_logs:/var/log/nginx:ro` từ Nginx Reverse Proxy.
- Tệp cấu hình `logging/promtail/promtail-config.yaml` định nghĩa job thu thập `job: nginx`, theo dõi liên tục hai tệp `access.log` và `error.log`.
- Promtail tự động gắn nhãn siêu dữ liệu `{job="nginx", env="production", service="reverse-proxy"}` cho từng dòng nhật ký và đẩy (Push) về API của Loki tại `http://loki:3100/loki/api/v1/push`.

## 5.3. Ngôn ngữ truy vấn LogQL và phân tích cú pháp
**LogQL (Log Query Language)** là ngôn ngữ truy vấn chính thống của Loki, có cấu trúc gồm:
1. **Bộ chọn luồng log (Log Stream Selector)**: Xác định nhóm log cần tìm dựa trên nhãn, ví dụ: `{job="nginx"}`.
2. **Bộ lọc dòng log (Log Pipeline / Filter Expression)**:
   - `|=`: Dòng log chứa chuỗi ký tự cụ thể.
   - `!=`: Dòng log không chứa chuỗi ký tự.
   - `|~`: Dòng log khớp với biểu thức chính quy (Regex match).
   - `!~`: Dòng log không khớp với biểu thức chính quy.
3. **Toán tử chuyển đổi chỉ số (Metric Query Operations)**:
   - `rate(...)`: Tính tốc độ xuất hiện của dòng log theo đơn vị giây.
   - `count_over_time(...)`: Đếm tổng số dòng log trong một khoảng thời gian trượt.

## 5.4. Hiện thực 5 câu truy vấn LogQL thực tế theo đề bài
Theo yêu cầu đề bài cần có ít nhất 2 - 3 câu truy vấn LogQL, dự án xây dựng và chuẩn hóa 5 câu truy vấn phục vụ quản trị và điều tra an ninh:

### 🟢 Câu truy vấn 1: Truy xuất toàn bộ dòng nhật ký của Nginx Reverse Proxy
```logql
{job="nginx"}
```
- **Mục đích**: Theo dõi toàn bộ dòng log thời gian thực phát sinh qua Reverse Proxy, bao gồm cả lượt truy cập bình thường và thông báo hệ thống.

### 🟡 Câu truy vấn 2: Lọc các yêu cầu HTTP gặp lỗi phía Khách hàng (4xx) hoặc Máy chủ (5xx)
```logql
{job="nginx"} |~ " (4\\d{2}|5\\d{2}) "
```
- **Mục đích**: Lọc ra các request bị lỗi như `403 Forbidden` (bị Nginx chặn), `404 Not Found` (không tìm thấy trang), `500 Internal Server Error`, `502 Bad Gateway` (WordPress hoặc upstream không phản hồi).

### 🔴 Câu truy vấn 3: Phát hiện các hành vi dò quét file nhạy cảm và tấn công XML-RPC (Security Alerts)
```logql
{job="nginx"} |= "403" or {job="nginx"} |= "xmlrpc.php"
```
- **Mục đích**: Giúp chuyên viên an ninh mạng (SOC/Security Analyst) lọc nhanh các sự kiện bị hệ thống Hardening từ chối truy cập và các nỗ lực xâm nhập trang quản trị.

### 📊 Câu truy vấn 4: Biến đổi Log thành Biểu đồ đo tốc độ phát sinh lỗi HTTP (Metric Query)
```logql
sum(rate({job="nginx"} |~ " (4\\d{2}|5\\d{2}) " [5m]))
```
- **Mục đích**: Biến đổi dòng log thành đồ thị chỉ số trên Grafana, hiển thị số lỗi phát sinh trên mỗi giây trong cửa sổ trượt 5 phút, dùng để kích hoạt cảnh báo khi tốc độ lỗi tăng đột biến.

### 🟣 Câu truy vấn 5: Lọc các thông báo lỗi và cảnh báo nghiêm trọng trong error.log
```logql
{job="nginx", filename=~".*error.log"} |= "error" or {job="nginx", filename=~".*error.log"} |= "warn"
```
- **Mục đích**: Hỗ trợ Quản trị viên hệ thống (SysAdmin) điều tra nguyên nhân sâu xa khi máy chủ Nginx gặp sự cố tải file cấu hình, lỗi bắt tay SSL hoặc mất kết nối mạng nội bộ.

\newpage

# CHƯƠNG 6: CÁC BIỆN PHÁP GIA CỐ VÀ BẢO MẬT HỆ THỐNG (HARDENING)

Gia cố hệ thống (Hardening) là yêu cầu kỹ thuật trọng tâm của đề tài nhằm đưa hệ thống từ mức độ "chạy được" lên mức độ "an toàn theo tiêu chuẩn sản xuất". Dự án triển khai 6 nhóm giải pháp gia cố:

## 6.1. Vận hành Non-Root Containers
Theo mặc định, nhiều container Docker chạy dưới quyền `root` (UID 0). Nếu kẻ tấn công khai thác được một lỗ hổng trong ứng dụng (ví dụ: Remote Code Execution - RCE), chúng sẽ sở hữu quyền root bên trong container và có nguy cơ cao thoát khỏi container (Container Escape) để chiếm quyền máy chủ host.
- **Prometheus**: Được cấu hình chạy với người dùng không đặc quyền `user: "nobody"` (UID 65534).
- **Loki**: Được cấu hình chạy với người dùng không đặc quyền `user: "10001:10001"`.
- Các tệp cấu hình được mount vào container dưới quyền chỉ đọc (`:ro - Read-Only`), ngăn chặn mã độc chỉnh sửa file cấu hình hệ thống ngay cả khi chiếm được shell.

## 6.2. Network Isolation & Bảo vệ Cổng Database
Trong mô hình bảo mật Zero Trust, không có bất kỳ thành phần nào được tin cậy tuyệt đối:
- Toàn bộ cổng dịch vụ của cơ sở dữ liệu MySQL (`cổng 3306`) **tuyệt đối không được khai báo ánh xạ (no ports binding)** ra ngoài máy chủ host trong `docker-compose.yml`.
- MySQL chỉ lắng nghe và giao tiếp bên trong mạng ảo nội bộ `net_production_backend`. Kẻ tấn công trên Internet quét cổng IP của máy chủ sẽ hoàn toàn không thấy cổng 3306 tồn tại, loại bỏ triệt để nguy cơ tấn công dò mật khẩu MySQL (Brute force) từ bên ngoài.

## 6.3. Nguyên tắc đặc quyền tối thiểu (Least Privilege)
Dự án áp dụng chặt chẽ nguyên tắc chỉ cấp phát quyền hạn vừa đủ để dịch vụ hoàn thành nhiệm vụ:
- Đối với WordPress: Sử dụng tài khoản người dùng `wp_user` với quyền hạn giới hạn chỉ trên duy nhất cơ sở dữ liệu `wordpress_db`, không có quyền quản trị máy chủ cơ sở dữ liệu.
- Đối với Prometheus MySQL Exporter: Thay vì sử dụng tài khoản `root`, hệ thống tạo một tài khoản riêng biệt `exporter` trong script `01-init.sql`:
  ```sql
  CREATE USER IF NOT EXISTS 'exporter'@'%' IDENTIFIED WITH mysql_native_password BY '...';
  GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';
  ALTER USER 'exporter'@'%' WITH MAX_USER_CONNECTIONS 5;
  ```
  Tài khoản này chỉ được cấp quyền đọc các chỉ số thống kê (`PROCESS, REPLICATION CLIENT, SELECT`), hoàn toàn bị cấm các lệnh chỉnh sửa cấu trúc hoặc thay đổi dữ liệu (`INSERT, UPDATE, DELETE, DROP`). Đồng thời giới hạn tối đa 5 kết nối đồng thời để không làm cạn kiệt tài nguyên hệ thống.

## 6.4. Quản lý bí mật an toàn với .env
- Tuyệt đối không lưu trữ thông tin mật khẩu, khóa bí mật (Secrets) hoặc chuỗi kết nối trực tiếp (hardcoded) bên trong mã nguồn hoặc tệp `docker-compose.yml`.
- Mọi thông tin nhạy cảm đều được tham chiếu qua biến môi trường.
- Tệp `.env` chứa mật khẩu thực tế được thêm vào `.gitignore` để không bao giờ bị lộ lên kho lưu trữ GitHub công khai. Dự án cung cấp tệp `.env.example` làm mẫu cấu hình chuẩn.

## 6.5. Gia cố bảo mật Nginx và triệt tiêu lỗ hổng WordPress
Nginx được tối ưu hóa thành một "bức tường lửa ứng dụng web cơ bản" (Lightweight WAF):
- `server_tokens off;`: Ẩn hoàn toàn phiên bản Nginx trong tiêu đề phản hồi `Server: nginx`, gây khó khăn cho kẻ tấn công khi tìm kiếm mã khai thác tương ứng với phiên bản.
- Chặn đứng tấn công XML-RPC (`/xmlrpc.php`).
- Ngăn chặn thực thi script PHP trong thư mục tải lên uploads: Khi quản trị viên hoặc người dùng upload tệp ảnh sản phẩm, nếu kẻ tấn công ngụy trang tệp `shell.php`, Nginx sẽ từ chối thực thi và trả về mã lỗi 403 Forbidden.
- Chặn đứng truy cập vào toàn bộ các tệp cấu hình ẩn như `.env`, `.git`, `.htaccess`.
- Triển khai đầy đủ 7 tiêu đề bảo mật HTTP (Security Headers) chuẩn OWASP.

\newpage

# CHƯƠNG 7: KỊCH BẢN KIỂM THỬ, ĐÁNH GIÁ VÀ HƯỚNG DẪN VẬN HÀNH

Dự án cung cấp bộ công cụ tự động hóa kiểm thử `scripts/test-system.ps1` (Windows PowerShell) và `scripts/test-system.sh` (Linux/Bash) nhằm kiểm tra toàn diện 4 kịch bản nghiệm thu:

## 7.1. Kịch bản kiểm thử chuyển hướng HTTPS và SSL
- **Mục tiêu**: Đảm bảo toàn bộ lưu lượng HTTP không an toàn đều bị cưỡng bức chuyển hướng sang HTTPS và chứng chỉ SSL hợp lệ.
- **Phương pháp thực hiện**: Sử dụng `curl` gửi yêu cầu tới cổng 80:
  ```bash
  curl -s -I http://localhost:80
  ```
- **Kết quả mong đợi & Thực tế**:
  ```http
  HTTP/1.1 301 Moved Permanently
  Server: nginx
  Date: Sat, 24 Oct 2026 15:30:00 GMT
  Content-Type: text/html
  Content-Length: 169
  Connection: keep-alive
  Location: https://localhost/
  ```
  Hệ thống phản hồi mã `301 Moved Permanently` với tiêu đề `Location: https://localhost/`. Khi kiểm tra chứng chỉ SSL qua lệnh OpenSSL, chứng chỉ hiển thị đầy đủ thông tin Subject Alternative Name (SAN) cho `localhost`, `127.0.0.1` và `wp.local`.

## 7.2. Kịch bản kiểm thử Security Headers
- **Mục tiêu**: Xác thực Nginx đã đính kèm đầy đủ các tiêu đề an ninh theo chuẩn OWASP.
- **Phương pháp thực hiện**: Gửi request kiểm tra tiêu đề phản hồi HTTPS:
  ```bash
  curl -k -s -I https://localhost:443
  ```
- **Kết quả nghiệm thu**:
  - `X-Frame-Options: SAMEORIGIN` -> **[PASS] Đạt**
  - `X-Content-Type-Options: nosniff` -> **[PASS] Đạt**
  - `X-XSS-Protection: 1; mode=block` -> **[PASS] Đạt**
  - `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload` -> **[PASS] Đạt**
  - `Referrer-Policy: strict-origin-when-cross-origin` -> **[PASS] Đạt**
  - `Content-Security-Policy: ...` -> **[PASS] Đạt**
  - `Permissions-Policy: ...` -> **[PASS] Đạt**

## 7.3. Kịch bản kiểm thử Hardening chặn XML-RPC và File nhạy cảm
- **Mục tiêu**: Kiểm chứng khả năng ngăn chặn các vector tấn công phổ biến vào WordPress.
- **Phương pháp thực hiện**:
  1. Gửi request thăm dò vào `https://localhost/xmlrpc.php`:
     ```bash
     curl -k -s -o /dev/null -w "%{http_code}" https://localhost/xmlrpc.php
     ```
     -> **Kết quả**: Trả về mã **`403 Forbidden`**. Kịch bản tấn công brute force XML-RPC bị triệt tiêu hoàn toàn.
  2. Gửi request thăm dò tệp môi trường `https://localhost/.env`:
     ```bash
     curl -k -s -o /dev/null -w "%{http_code}" https://localhost/.env
     ```
     -> **Kết quả**: Trả về mã **`403 Forbidden`**. Thông tin nhạy cảm được bảo vệ an toàn.

## 7.4. Kịch bản kiểm thử truy vấn LogQL trên Grafana Explore
- **Mục tiêu**: Đảm bảo dòng nhật ký truy cập và sự kiện lỗi được Promtail đẩy về Loki và có thể truy vấn nhanh chóng bằng ngôn ngữ LogQL.
- **Phương pháp thực hiện**:
  1. Truy cập giao diện Grafana tại `https://localhost/grafana/` hoặc `http://localhost:3000`.
  2. Vào mục **Explore**, chọn nguồn dữ liệu **Loki**.
  3. Nhập câu truy vấn lọc lỗi: `{job="nginx"} |~ " (4\\d{2}|5\\d{2}) "`
- **Kết quả nghiệm thu**:
  - Bảng Log Volume Histogram hiển thị các cột thời gian phát sinh lỗi.
  - Khung Log Streams hiển thị chi tiết địa chỉ IP máy khách, thời điểm truy cập, phương thức HTTP GET/POST, URL yêu cầu và User-Agent tương ứng.

## 7.5. Hướng dẫn vận hành và bảo trì hệ thống
Quy trình vận hành hệ thống được chuẩn hóa qua các lệnh đơn giản:

| Thao tác | Lệnh thực hiện trên Terminal |
| :--- | :--- |
| **Khởi động toàn bộ hệ thống** | `docker compose up -d` |
| **Kiểm tra trạng thái container** | `docker compose ps` |
| **Xem log thời gian thực** | `docker compose logs -f [tên_dịch_vụ]` |
| **Kiểm thử hệ thống tự động** | `powershell -ExecutionPolicy Bypass -File .\scripts\test-system.ps1` |
| **Dừng hệ thống tạm thời** | `docker compose stop` |
| **Tắt và dọn dẹp hệ thống** | `docker compose down` |
| **Sao lưu cơ sở dữ liệu MySQL** | `docker exec production-mysql mysqldump -u root -p[password] wordpress_db > backup.sql` |
| **Phục hồi cơ sở dữ liệu** | `docker exec -i production-mysql mysql -u root -p[password] wordpress_db < backup.sql` |

\newpage

# CHƯƠNG 8: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 8.1. Các kết quả đã hoàn thành
Trải qua quá trình nghiên cứu và thực nghiệm nghiêm túc, đề tài đã hoàn thành xuất sắc 100% các yêu cầu kỹ thuật do giảng viên đề ra:
1. **Xây dựng thành công ngăn xếp ứng dụng WordPress hoàn chỉnh**: Ứng dụng giới thiệu sản phẩm vận hành mượt mà, tích hợp cơ sở dữ liệu MySQL 8.0 tối ưu hiệu năng và công cụ quản trị phpMyAdmin an toàn.
2. **Triển khai kiến trúc Nginx Reverse Proxy chuẩn hóa**: Bảo vệ hệ thống bằng kết nối HTTPS tự ký có SAN, chuyển hướng HTTP 301, bộ quy tắc bảo mật Security Headers, và kiểm soát lưu lượng chống brute force.
3. **Hiện thực hệ thống giám sát đa tầng Prometheus + Grafana**: Thu thập đầy đủ số liệu từ phần cứng, container, database và web server; tự động nạp các bảng điều khiển (Dashboards) trực quan không cần can thiệp thủ công.
4. **Hiện thực giải pháp quản trị nhật ký tập trung Loki + Promtail**: Thu thập toàn bộ access/error logs và xây dựng bộ 5 câu truy vấn LogQL chuyên sâu cho điều tra sự cố và giám sát an ninh.
5. **Gia cố bảo mật hệ thống toàn diện (Hardening)**: Thực thi cô lập mạng 3 tầng (Network Isolation), khóa cổng cơ sở dữ liệu, phân quyền tối thiểu (Least Privilege), chạy container dưới người dùng non-root và quản lý biến môi trường an toàn.
6. **Lập tài liệu và quản lý phiên bản chuyên nghiệp**: Mã nguồn được quản lý trên Git với lịch sử commit rõ ràng theo từng giai đoạn kỹ thuật, tài liệu hướng dẫn README chi tiết và báo cáo khoa học đầy đủ.

## 8.2. Hạn chế và Hướng mở rộng
Mặc dù hệ thống đã đáp ứng tốt các tiêu chuẩn môi trường sản xuất cơ bản, một số định hướng phát triển có thể được nghiên cứu nâng cấp trong tương lai:
- **Tự động gia hạn chứng chỉ SSL**: Tích hợp module Certbot / Let's Encrypt với giao thức ACME để tự động phát hành và gia hạn chứng chỉ SSL hợp lệ có chữ ký tin cậy trên Internet khi đưa ra tên miền thật.
- **Hệ thống điều phối quy mô lớn (Kubernetes)**: Chuyển đổi mô hình Docker Compose sang Kubernetes (K8s) với Deployment, StatefulSet, Ingress Controller và Horizontal Pod Autoscaler (HPA) để tự động co giãn số lượng container theo tải thực tế.
- **Tích hợp Web Application Firewall chuyên sâu (ModSecurity / Coraza WAF)**: Nhúng bộ quy tắc Core Rule Set (OWASP CRS) vào Nginx để phòng chống các đợt tấn công SQL Injection và Remote Code Execution tinh vi.
- **Hệ thống cảnh báo tự động (Alertmanager)**: Tích hợp Prometheus Alertmanager gửi thông báo khẩn cấp qua kênh Telegram hoặc Discord của đội ngũ quản trị viên khi phát hiện sập dịch vụ hoặc CPU vượt ngưỡng 85%.

\newpage

# TÀI LIỆU THAM KHẢO

1. **Docker Documentation**, *Docker Compose File Reference & Best Practices for Production*, 2026. [Online]. Có sẵn: https://docs.docker.com/compose/
2. **Nginx Documentation**, *Configuring NGINX as an HTTP Reverse Proxy & SSL Termination*, 2026. [Online]. Có sẵn: https://nginx.org/en/docs/
3. **Prometheus Authors**, *Prometheus - Monitoring system & Time Series Database Architecture*, 2026. [Online]. Có sẵn: https://prometheus.io/docs/
4. **Grafana Labs**, *Grafana Loki - Like Prometheus, but for Logs & LogQL Reference*, 2026. [Online]. Có sẵn: https://grafana.com/docs/loki/latest/
5. **OWASP Foundation**, *OWASP Secure Headers Project & Web Security Testing Guide*, 2026. [Online]. Có sẵn: https://owasp.org/www-project-secure-headers/
6. **WordPress Codex & Developer Resources**, *Hardening WordPress & Operating Behind Reverse Proxies*, 2026. [Online]. Có sẵn: https://developer.wordpress.org/advanced-administration/security/hardening/
7. **Center for Internet Security (CIS)**, *CIS Docker Benchmark for Security Configuration*, Version 1.6.0, 2025.
