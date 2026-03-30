# 🛰️ PhoneRecon — Advanced Number Intelligence Toolkit

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OSINT-Tool-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/CLI-Based-black?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/your-username/phonerecon?style=for-the-badge">
</p>

<p align="center">
Lightweight • Fast • Developer-Friendly • OSINT Powered
</p>

---

## ⚡ About PhoneRecon

**PhoneRecon** is a modern CLI-based OSINT tool designed to extract intelligence from phone numbers using public data sources and telecom metadata.

Built for:

* 🧑‍💻 Developers
* 🔐 Security researchers
* 🕵️ OSINT enthusiasts

---

## ✨ Features

* 🌍 Global phone number parsing & validation
* 📡 Carrier/operator detection
* 📍 Region & country identification
* 🕰️ Timezone extraction
* 📱 Line type detection (Mobile / VoIP / Landline)
* 💬 WhatsApp registration check (best-effort)
* 🚫 Spam reputation lookup
* 📄 JSON export (developer-friendly)
* ⚡ Fast CLI execution

---

## 🧠 Internal Workflow

```bash
parse → build → enrich → output
```

* **Parse** → Validate & normalize number
* **Build** → Extract telecom metadata
* **Enrich** → Add OSINT signals
* **Output** → CLI or JSON

---

## 📲 Installation — Termux (Android)

### Step by Step

```bash
pkg update && pkg upgrade -y
```

```bash
pkg install git -y
```

```bash
git clone https://github.com/thakur2309/phonextract.git
```

```bash
cd phonextract
```

```bash
pip install -r requirements.txt
```

```bash
python3 phonextract.py
```

### ⚡ One-Line Install (Termux)

```bash
pkg update && pkg upgrade && pkg install git && git clone https://github.com/thakur2309/phonextract.git && cd phonextract && pip install -r requirements.txt && python3 phonextract.py
```

---

## 🐉 Installation — Kali Linux (Using venv)

> On Kali Linux, system-wide `pip install` is restricted. It is recommended to use a **Python virtual environment (venv)** to avoid errors.

### Step 1 — Update your system

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2 — Install required packages

```bash
sudo apt install python3-venv python3-pip git -y
```

### Step 3 — Clone the repository

```bash
git clone https://github.com/rishimistry/phonerecon.git
```

### Step 4 — Navigate into the folder

```bash
cd phonerecon
```

### Step 5 — Create a virtual environment

```bash
python3 -m venv venv
```

### Step 6 — Activate the virtual environment

```bash
source venv/bin/activate
```

> ✅ You will see `(venv)` at the start of your terminal — this means the virtual environment is active.

### Step 7 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 8 — Run the tool

```bash
python3 phonerecon.py
```

### ⚡ One-Line Install (Kali Linux)

```bash
sudo apt update && sudo apt install python3-venv python3-pip git -y && git clone https://github.com/rishimistry/phonerecon.git && cd phonerecon && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python3 phonerecon.py
```

### 🔁 Run Again Next Time — Kali Linux

Every time you want to use the tool again:

```bash
cd phonerecon
source venv/bin/activate
python3 phonerecon.py
```

### ❌ Deactivate Virtual Environment

```bash
deactivate
```

---

## 🖥️ Installation — Ubuntu / Debian / Parrot OS

```bash
sudo apt update && sudo apt install python3-venv python3-pip git -y
git clone https://github.com/rishimistry/phonerecon.git
cd phonerecon
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 phonerecon.py
```

---

## 🪟 Installation — Windows

### Requirements
- Python 3.x — Download from [python.org](https://www.python.org/downloads/)
- Git — Download from [git-scm.com](https://git-scm.com/)

### Steps

```cmd
git clone https://github.com/rishimistry/phonerecon.git
cd phonerecon
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python phonerecon.py
```

## 🖥️ Supported Platforms

* 🐧 Linux (Kali, Ubuntu, Parrot)
* 🪟 Windows
* 📱 Termux

---

## ⚠️ Disclaimer

This tool is strictly for:

* Educational purposes
* Ethical OSINT
* Security research

### Important Notes:

* 📍 Location is **prefix-based**, not real-time GPS
* 📡 Carrier data may be outdated (MNP issue)
* 💬 WhatsApp detection is not 100% reliable
* 🚫 Spam data is scraped from public sources
* ❗ Results may not always be accurate

> Use responsibly and verify critical data from official sources.

---

## 🧑‍💻 Tech Stack

* Python 3
* phonenumbers
* requests
* argparse

---

## 🔮 Roadmap

* 🌐 Web Dashboard (Flask / FastAPI)
* ⚡ Async scanning engine
* 🧠 AI spam detection
* 📊 Risk scoring system
* 🔗 REST API mode

---

## 🤝 Contributing

Pull requests are welcome.

You can contribute in:

* Performance improvements
* OSINT integrations
* Feature enhancements

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Share it

---

## 🙏 Credits

This project is inspired by the original tool PhoneXtract.

Original Developer: Alok Thakur
Original Project: PhoneXtract

---

<p align="center">
Built with ⚡ by developers, for developers
</p>
