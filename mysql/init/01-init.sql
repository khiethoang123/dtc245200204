-- ==============================================================================
-- KHỞI TẠO CƠ SỞ DỮ LIỆU & PHÂN QUYỀN TỐI THIỂU (LEAST PRIVILEGE) CHO MYSQL
-- ==============================================================================

-- 1. Đảm bảo Database WordPress tồn tại
CREATE DATABASE IF NOT EXISTS `wordpress_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Tạo tài khoản riêng biệt cho Prometheus MySQL Exporter với quyền tối thiểu (Least Privilege)
-- Tài khoản này chỉ được cấp quyền đọc thống kê hệ thống (PROCESS, REPLICATION CLIENT, SELECT),
-- TUYỆT ĐỐI không có quyền INSERT, UPDATE, DELETE hay DROP dữ liệu!
CREATE USER IF NOT EXISTS 'exporter'@'%' IDENTIFIED WITH mysql_native_password BY 'Exporter_Secure_P@ss_2026!';
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';

-- 3. Giới hạn số lượng truy vấn tối đa của user exporter để không ảnh hưởng hiệu năng production
ALTER USER 'exporter'@'%' WITH MAX_USER_CONNECTIONS 5;

FLUSH PRIVILEGES;
