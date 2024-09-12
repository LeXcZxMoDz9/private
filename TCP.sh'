#!/bin/bash

HOST=$1
PORT=$2
TIME=$3

# Memeriksa apakah port adalah 443 atau 80
if [ "$PORT" -eq 443 ] || [ "$PORT" -eq 80 ]; then
    echo "Blacklist target"
else
    # Jika port bukan 443 atau 80, jalankan perintah ./TCP
    ./TCP "$HOST" "$PORT" "$TIME"
fi
