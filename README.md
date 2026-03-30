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

## 🚀 Usage

### 🔍 Scan a Number

```bash
python main.py scan +919876543210
```

---

### 📦 Batch Scan

```bash
python main.py batch numbers.txt
```

---

### 📄 Export JSON

```bash
python main.py scan +919876543210 --json
```

---

### ℹ️ Info

```bash
python main.py info
```

---

## 📁 Input Format

Always use **international format**:

| Country    | Example       |
| ---------- | ------------- |
| 🇮🇳 India | +919876543210 |
| 🇺🇸 USA   | +14155552671  |
| 🇬🇧 UK    | +447911123456 |

---

## 🛠️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/rishimistry/phonerecon.git
cd phonerecon
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Tool

```bash
python main.py scan +919876543210
```

---

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

<p align="center">
Built with ⚡ by developers, for developers
</p>
