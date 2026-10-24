#!/usr/bin/env bash
# ==============================================================================
# SCRIPT KHỞI ĐỘNG HỆ THỐNG TỰ ĐỘNG TRÊN LINUX / WSL
# ==============================================================================
set -e

echo "=================================================================="
echo "   KHOA CÔNG NGHỆ THÔNG TIN - MÔN TRIỂN KHAI VÀ QUẢN TRỊ HT SOFTWARE"
echo "   KHỞI ĐỘNG HỆ THỐNG ĐỀ TÀI 3: WORDPRESS PRODUCTION STACK"
echo "=================================================================="

# 1. Kiểm tra file .env
if [ ! -f ".env" ]; then
    echo "[+] Chưa tìm thấy file .env, tiến hành sao chép từ .env.example..."
    cp .env.example .env
    echo "[OK] Đã tạo file .env thành công!"
fi

# 2. Kiểm tra chứng chỉ SSL
if [ ! -f "nginx/ssl/selfsigned.crt" ] || [ ! -f "nginx/ssl/selfsigned.key" ]; then
    echo "[+] Chưa tìm thấy chứng chỉ SSL, đang khởi tạo..."
    chmod +x nginx/ssl/generate-cert.sh
    ./nginx/ssl/generate-cert.sh
    echo "[OK] Đã tạo chứng chỉ SSL tự ký thành công!"
fi

# 3. Khởi động các container qua Docker Compose
echo "[+] Đang khởi động toàn bộ stack dịch vụ bằng Docker Compose..."
docker compose up -d

echo "=================================================================="
echo "   KHỞI ĐỘNG HỆ THỐNG THÀNH CÔNG! CÁC ĐỊA CHỈ TRUY CẬP:"
echo "   - WordPress Website:    https://localhost"
echo "   - phpMyAdmin Database:  https://localhost/pma/"
echo "   - Grafana Dashboard:    https://localhost/grafana/ (hoặc http://localhost:3000)"
echo "   - Prometheus Metrics:   http://localhost:9090"
echo "   - Loki Logs:            http://localhost:3100"
echo "=================================================================="
