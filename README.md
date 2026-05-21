# Automated Recon Tool

Automated reconnaissance framework built using Python for passive and active information gathering on target domains.

## Features

* Subdomain Enumeration using Sublist3r
* DNS Bruteforcing
* Email Harvesting with theHarvester
* OSINT Collection
* Shodan API Integration
* Technology Fingerprinting
* HTML Report Generation
* PDF Report Generation

---

## Technologies Used

* Python
* Sublist3r
* theHarvester
* Shodan API
* BuiltWith
* WeasyPrint
* Jinja2

---

## Project Structure

```bash
recon-tool/
│
├── modules/
│   ├── subdomain_enum.py
│   ├── dns_bruteforce.py
│   ├── email_osint.py
│   ├── shodan_lookup.py
│   ├── tech_fingerprint.py
│   └── report_generator.py
│
├── templates/
│   └── report_template.html
│
├── wordlists/
│   └── subdomains.txt
│
├── reports/
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/VR25-coder/Automated-Recon-Tool.git
cd Automated-Recon-Tool
```

---

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the tool:

```bash
python3 main.py
```

Enter target domain:

```bash
example.com
```

---

## Example Workflow

```text
Target Domain
      ↓
Subdomain Enumeration
      ↓
DNS Bruteforcing
      ↓
OSINT Collection
      ↓
Technology Fingerprinting
      ↓
Shodan Lookup
      ↓
HTML/PDF Report Generation
```

---

## Output

Generated reports are saved inside:

```bash
reports/
```

Files generated:

* report.html
* report.pdf

---

## Screenshots

### Terminal Output

(Add screenshot here)

### HTML Report

(Add screenshot here)

### PDF Report

(Add screenshot here)

---

## Skills Demonstrated

* Cybersecurity
* OSINT
* Reconnaissance
* Python Automation
* DNS Enumeration
* API Integration
* Report Automation
* Ethical Hacking

---

## Future Improvements

* Flask Dashboard
* Nmap Integration
* CVE Detection
* Multi-threading
* Streamlit UI
* Docker Support
* JSON Export
* Vulnerability Scanning

---

## Disclaimer

This project is intended for educational and authorized security testing purposes only.

Do not use against systems without permission.

---

## Author

Vrutant Ratanpure

GitHub: https://github.com/VR25-coder
