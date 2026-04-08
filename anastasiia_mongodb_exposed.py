# ============================================================
#  Author: Anastasiia Stoianova
#  Vulnerability: MongoDB exposed without authentication
#  Target: mongo.0x10.cloud
# ============================================================

import socket

target = "mongo.0x10.cloud"
port = 27017

print("=" * 50)
print("  Open Port Check (MongoDB)")
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
        print(f"  Port {port} (MongoDB) is OPEN on {target}")
        print(f"  MongoDB is exposed with no authentication.")
        print(f"  Attackers can access or delete all data.")
    else:
        print(f"\n  [OK] Port {port} is closed on {target}")

    sock.close()

except socket.error as e:
    print(f"\n  [ERROR] Could not connect: {e}")
