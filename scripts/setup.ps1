# ==============================================================================
# SCRIPT KHỞI ĐỘNG HỆ THỐNG TỰ ĐỘNG TRÊN WINDOWS POWERSHELL
# ==============================================================================
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "   KHOA CÔNG NGHỆ THÔNG TIN - MÔN TRIỂN KHAI VÀ QUẢN TRỊ HT SOFTWARE" -ForegroundColor Cyan
Write-Host "   KHỞI ĐỘNG HỆ THỐNG ĐỀ TÀI 3: WORDPRESS PRODUCTION STACK" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

# 1. Kiểm tra file .env
if (-not (Test-Path ".env")) {
    Write-Host "[+] Chưa tìm thấy file .env, tiến hành sao chép từ .env.example..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "[OK] Đã tạo file .env thành công!" -ForegroundColor Green
}

# 2. Kiểm tra chứng chỉ SSL
if (-not (Test-Path "nginx\ssl\selfsigned.crt") -or -not (Test-Path "nginx\ssl\selfsigned.key")) {
    Write-Host "[+] Chưa tìm thấy chứng chỉ SSL, đang khởi tạo..." -ForegroundColor Yellow
    powershell -ExecutionPolicy Bypass -File .\nginx\ssl\generate-cert.ps1
    Write-Host "[OK] Đã tạo chứng chỉ SSL tự ký thành công!" -ForegroundColor Green
}

# 3. Khởi động các container qua Docker Compose
Write-Host "[+] Đang khởi động toàn bộ stack dịch vụ bằng Docker Compose..." -ForegroundColor Yellow
docker compose up -d

Write-Host "==================================================================" -ForegroundColor Green
Write-Host "   KHỞI ĐỘNG HỆ THỐNG THÀNH CÔNG! CÁC ĐỊA CHỈ TRUY CẬP:" -ForegroundColor Green
Write-Host "   - WordPress Website:    https://localhost" -ForegroundColor White
Write-Host "   - phpMyAdmin Database:  https://localhost/pma/" -ForegroundColor White
Write-Host "   - Grafana Dashboard:    https://localhost/grafana/ (hoặc http://localhost:3000)" -ForegroundColor White
Write-Host "   - Prometheus Metrics:   http://localhost:9090" -ForegroundColor White
Write-Host "   - Loki Logs:            http://localhost:3100" -ForegroundColor White
Write-Host "==================================================================" -ForegroundColor Green
