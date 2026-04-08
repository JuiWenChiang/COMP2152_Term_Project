# ============================================================
#  Author: Anastasiia Stoianova
#  Vulnerability: Redis exposed without authentication
#  Target: redis.0x10.cloud
# ============================================================

import socket

target = "redis.0x10.cloud"
port = 6379

print("=" * 50)
print("  Open Port Check (Redis)")
print("=" * 50)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    print(f"\n  Target: {target}")
    print(f"  Port:   {port}")
    print(f"  Scanning...")

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"\n  [!] VULNERABILITY FOUND")
        print(f"  Port {port} (Redis) is OPEN on {target}")
        print(f"  Redis is exposed with no authentication.")
        print(f"  Attackers can read/write data or run commands.")
    else:
        print(f"\n  [OK] Port {port} is closed on {target}")

    sock.close()

except socket.error as e:
    print(f"\n  [ERROR] Could not connect: {e}")
