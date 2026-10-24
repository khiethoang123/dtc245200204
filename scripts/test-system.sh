#!/usr/bin/env bash
# ==============================================================================
# SCRIPT KIỂM THỬ HỆ THỐNG & KIỂM TRA BẢO MẬT TỰ ĐỘNG TRÊN LINUX / WSL
# ==============================================================================
set -e

echo "=================================================================="
echo "        BẮT ĐẦU KIỂM THỬ TOÀN DIỆN HỆ THỐNG ĐỀ TÀI 3"
echo "=================================================================="

# 1. Kiểm tra chuyển hướng 301
echo -e "\n[1] Kiểm tra chuyển hướng 301 từ HTTP 80 sang HTTPS 443..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:80 || true)
if [ "$HTTP_CODE" = "301" ]; then
    echo "  -> [PASS] HTTP 80 đã chuyển hướng 301 sang HTTPS!"
else
    echo "  -> [INFO] HTTP Status: $HTTP_CODE"
fi

# 2. Kiểm tra HTTPS và Security Headers
echo -e "\n[2] Kiểm tra kết nối HTTPS và các Security Headers bảo mật..."
HEADERS=$(curl -k -s -I https://localhost:443 || true)
for H in "X-Frame-Options" "X-Content-Type-Options" "X-XSS-Protection" "Strict-Transport-Security" "Referrer-Policy" "Content-Security-Policy"; do
    if echo "$HEADERS" | grep -iq "$H"; then
        echo "  -> [PASS] Đã tìm thấy header: $H"
    else
        echo "  -> [WARN] Chưa tìm thấy header: $H"
    fi
done

# 3. Kiểm tra Hardening chặn xmlrpc.php
echo -e "\n[3] Kiểm tra Hardening: Chặn truy cập /xmlrpc.php..."
XML_CODE=$(curl -k -s -o /dev/null -w "%{http_code}" https://localhost:443/xmlrpc.php || true)
if [ "$XML_CODE" = "403" ]; then
    echo "  -> [PASS] /xmlrpc.php đã bị chặn thành công với mã 403 Forbidden!"
else
    echo "  -> [INFO] Phản hồi: $XML_CODE"
fi

# 4. Kiểm tra các dịch vụ Giám sát
echo -e "\n[4] Kiểm tra các dịch vụ Giám sát & Quản trị..."
curl -s -o /dev/null -w "  -> Prometheus Health: %{http_code}\n" http://localhost:9090/-/healthy || true
curl -s -o /dev/null -w "  -> Grafana Health: %{http_code}\n" http://localhost:3000/api/health || true
curl -s -o /dev/null -w "  -> Loki Health: %{http_code}\n" http://localhost:3100/ready || true

echo -e "\n=================================================================="
echo "                    HOÀN TẤT KIỂM THỬ HỆ THỐNG"
echo "=================================================================="
