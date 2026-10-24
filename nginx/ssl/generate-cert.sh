#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
CNF_PATH="$DIR/openssl.cnf"

cat > "$CNF_PATH" << 'EOF'
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
EOF

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout "$DIR/selfsigned.key" \
    -out "$DIR/selfsigned.crt" \
    -config "$CNF_PATH"

chmod 644 "$DIR/selfsigned.crt"
chmod 600 "$DIR/selfsigned.key"

echo "SSL Certificate generated successfully in $DIR"
