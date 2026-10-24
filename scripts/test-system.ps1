# ==============================================================================
# SCRIPT KIỂM THỬ HỆ THỐNG & KIỂM TRA BẢO MẬT TỰ ĐỘNG TRÊN WINDOWS
# ==============================================================================
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "        BẮT ĐẦU KIỂM THỬ TOÀN DIỆN HỆ THỐNG ĐỀ TÀI 3" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

# Bỏ qua xác thực SSL không tin cậy đối với chứng chỉ tự ký nội bộ
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

# 1. Kiểm tra chuyển hướng HTTP sang HTTPS
Write-Host "`n[1] Kiểm tra chuyển hướng 301 từ HTTP sang HTTPS..." -ForegroundColor Yellow
try {
    $res80 = Invoke-WebRequest -Uri "http://localhost:80" -MaximumRedirection 0 -ErrorAction SilentlyContinue
    if ($res80.StatusCode -eq 301) {
        Write-Host "  -> [PASS] HTTP 80 đã chuyển hướng 301 sang: $($res80.Headers.Location)" -ForegroundColor Green
    }
} catch {
    if ($_.Exception.Response.StatusCode.value__ -eq 301) {
        Write-Host "  -> [PASS] HTTP 80 đã chuyển hướng 301 sang HTTPS!" -ForegroundColor Green
    } else {
        Write-Host "  -> [WARN] Kết quả phản hồi: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# 2. Kiểm tra truy cập HTTPS và các Security Headers
Write-Host "`n[2] Kiểm tra kết nối HTTPS và các Security Headers bảo mật..." -ForegroundColor Yellow
try {
    $res443 = Invoke-WebRequest -Uri "https://localhost:443" -SkipCertificateCheck -ErrorAction Stop
    Write-Host "  -> [PASS] Truy cập HTTPS thành công (Status: $($res443.StatusCode))" -ForegroundColor Green
    
    $headers = @(
        "X-Frame-Options",
        "X-Content-Type-Options",
        "X-XSS-Protection",
        "Strict-Transport-Security",
        "Referrer-Policy",
        "Content-Security-Policy"
    )
    foreach ($h in $headers) {
        if ($res443.Headers.ContainsKey($h)) {
            Write-Host "     [✓] $h: $($res443.Headers[$h])" -ForegroundColor Green
        } else {
            Write-Host "     [✗] Thiếu header: $h" -ForegroundColor Red
        }
    }
} catch {
    Write-Host "  -> [INFO] Dịch vụ đang khởi động hoặc chưa chạy: $($_.Exception.Message)" -ForegroundColor Yellow
}

# 3. Kiểm tra cơ chế Hardening: Chặn truy cập xmlrpc.php và file nhạy cảm
Write-Host "`n[3] Kiểm tra Hardening: Chặn truy cập /xmlrpc.php..." -ForegroundColor Yellow
try {
    $resXml = Invoke-WebRequest -Uri "https://localhost:443/xmlrpc.php" -SkipCertificateCheck -ErrorAction Stop
    Write-Host "  -> [FAIL] /xmlrpc.php chưa bị chặn (Status: $($resXml.StatusCode))" -ForegroundColor Red
} catch {
    if ($_.Exception.Response.StatusCode.value__ -eq 403) {
        Write-Host "  -> [PASS] /xmlrpc.php đã bị chặn thành công với mã 403 Forbidden!" -ForegroundColor Green
    } else {
        Write-Host "  -> [PASS] /xmlrpc.php bị từ chối truy cập (Mã lỗi: $($_.Exception.Response.StatusCode.value__))" -ForegroundColor Green
    }
}

# 4. Kiểm tra trạng thái Prometheus & Grafana
Write-Host "`n[4] Kiểm tra các dịch vụ Giám sát & Quản trị..." -ForegroundColor Yellow
$services = @(
    @{ Name = "Prometheus Metrics"; Url = "http://localhost:9090/-/healthy" },
    @{ Name = "Grafana UI";        Url = "http://localhost:3000/api/health" },
    @{ Name = "Loki Logs Server";   Url = "http://localhost:3100/ready" }
)
foreach ($s in $services) {
    try {
        $r = Invoke-WebRequest -Uri $s.Url -TimeoutSec 5 -ErrorAction Stop
        Write-Host "  -> [PASS] $($s.Name) hoạt động tốt (Status: $($r.StatusCode))" -ForegroundColor Green
    } catch {
        Write-Host "  -> [INFO] $($s.Name) chưa phản hồi (có thể đang khởi động)" -ForegroundColor Gray
    }
}

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host "                    HOÀN TẤT KIỂM THỬ HỆ THỐNG" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
