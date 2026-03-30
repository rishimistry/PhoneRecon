import argparse
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, is_valid_number, format_number, PhoneNumberFormat
import requests
import time
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def header():
    print("\nPhoneRecon :: Number Intelligence Toolkit")
    print("-" * 45)


def section(title):
    print(f"\n[{title}]")


def probe_whatsapp(e164):
    try:
        clean = e164.replace("+", "")
        r = requests.get(f"https://wa.me/{clean}", headers=HEADERS, timeout=5)
        text = r.text.lower()
        if "not on whatsapp" in text or "invalid" in text:
            return "Not Registered"
        return "Registered"
    except:
        return "Unknown"


def fetch_spam_data(e164):
    try:
        url = f"https://www.shouldianswer.com/phone-number/{e164.replace('+','')}"
        r = requests.get(url, headers=HEADERS, timeout=5)
        text = r.text.lower()
        if "scam" in text:
            return "Scam"
        if "spam" in text:~
            return "Spam"
        return "No Reports"
    except:
        return "Unavailable"


def build_data(parsed):
    e164 = format_number(parsed, PhoneNumberFormat.E164)
    return {
        "number": e164,
        "country": geocoder.description_for_number(parsed, "en"),
        "carrier": carrier.name_for_number(parsed, "en"),
        "timezone": list(timezone.time_zones_for_number(parsed)),
        "type": number_type(parsed)
    }


def enrich_data(data):
    data["whatsapp"] = probe_whatsapp(data["number"])
    data["spam"] = fetch_spam_data(data["number"])
    return data


def display(data):
    for k, v in data.items():
        print(f"{k:15}: {v}")


def export_json(data):
    fname = f"report_{int(time.time())}.json"
    with open(fname, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\nSaved: {fname}")


def run_scan(target, save_json=False):
    try:
        parsed = phonenumbers.parse(target, None)
        if not is_valid_number(parsed):
            print("Invalid number")
            return
    except:
        print("Parsing failed")
        return

    header()
    section("Processing")
    time.sleep(0.5)

    data = build_data(parsed)
    data = enrich_data(data)

    section("Result")
    display(data)

    if save_json:
        export_json(data)


def run_batch(file_path):
    try:
        with open(file_path) as f:
            numbers = [x.strip() for x in f if x.strip()]
    except:
        print("File error")
        return

    for num in numbers:
        run_scan(num)
        print("\n" + "-" * 30)


def show_info():
    header()
    print("CLI OSINT tool for phone number intelligence")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PhoneRecon CLI")
    parser.add_argument("mode", choices=["scan", "batch", "info"])
    parser.add_argument("input", nargs="?")
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.mode == "scan":
        run_scan(args.input, args.json)
    elif args.mode == "batch":
        run_batch(args.input)
    elif args.mode == "info":
        show_info()
