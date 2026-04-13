# Author: Fatemeh Ghaani
# Vulnerability: HTTP instead of HTTPS
# Target: blog.0x10.cloud

import urllib.request

try:
    url = "http://api.0x10.cloud"
    response = urllib.request.urlopen(url)

    print(f"Status: {response.status}")
    print(f"Final URL: {response.url}")

    if response.url.startswith("http://"):
        print("VULNERABILITY FOUND: Website is not using HTTPS!")
    else:
        print("Secure: Using HTTPS")

except Exception as e:
    print(f"Error: {e}")