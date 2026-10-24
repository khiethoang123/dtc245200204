# Script to generate Self-Signed SSL Certificate with SAN for localhost
$certDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$opensslBin = "C:\Program Files\Git\usr\bin\openssl.exe"
if (-not (Test-Path $opensslBin)) {
    $opensslBin = "openssl"
}

$cnfPath = Join-Path $certDir "openssl.cnf"
@"
[req]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn
x509_extensions = v3_req

[dn]
C = VN
ST = HaNoi
L = HaNoi
O = University
OU = IT_Department
CN = localhost

[v3_req]
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = *.localhost
DNS.3 = wp.local
DNS.4 = pma.local
IP.1 = 127.0.0.1
IP.2 = ::1
"@ | Out-File -FilePath $cnfPath -Encoding utf8

$keyPath = Join-Path $certDir "selfsigned.key"
$crtPath = Join-Path $certDir "selfsigned.crt"

& $opensslBin req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $keyPath -out $crtPath -config $cnfPath

Write-Host "SSL Certificate generated successfully at:" -ForegroundColor Green
Write-Host "Certificate: $crtPath"
Write-Host "Private Key: $keyPath"
