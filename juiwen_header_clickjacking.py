# ============================================================
# Author: Jui-Wen Chiang
# Vulnerability: Clickjacking (Missing X-Frame-Options Header)
# Target: blog.0x10.cloud
# ============================================================
import urllib.request
import urllib.error

target = "blog.0x10.cloud"

print("=" * 60)
print("  Clickjacking Vulnerability Check")
print("=" * 60)

try:
    print(f"\n  Target: {target}")

    req = urllib.request.Request(f"http://{target}")
    req.add_header("User-Agent", "Mozilla/5.0")

    try:
        response = urllib.request.urlopen(req, timeout=5)
        headers = dict(response.headers)
    except urllib.error.HTTPError as e:
        headers = dict(e.headers)

    x_frame = headers.get("X-Frame-Options")
    csp = headers.get("Content-Security-Policy")

    print(f"\n  X-Frame-Options          : {x_frame or 'NOT PRESENT'}")
    print(f"  Content-Security-Policy  : {csp or 'NOT PRESENT'}")

    if not x_frame and not csp:
        print("""
      [!] VULNERABILITY FOUND: Clickjacking
      The site does not set X-Frame-Options or CSP frame-ancestors.
      This allows attackers to embed the site inside an <iframe>
      and trick users into clicking hidden UI elements.
        """)
    else:
        print("\n  [OK] Site is protected against Clickjacking.")

except Exception as e:
    print(f"  [ERROR] {e}")

print("=" * 60)