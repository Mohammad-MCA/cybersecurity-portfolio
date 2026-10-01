# 🔒 Google Cybersecurity Professional Certificate Portfolio

> A complete, job-ready portfolio showcasing hands-on projects and skills from the **Google Cybersecurity Professional Certificate** (Coursera).

[![Status](https://img.shields.io/badge/status-complete-brightgreen)](https://github.com)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Google](https://img.shields.io/badge/Google-Cybersecurity-4285F4)](https://grow.google/certificates/cybersecurity/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](./08-python-automation/)
[![Linux](https://img.shields.io/badge/Linux-CLI-FCC624?logo=linux&logoColor=black)](./04-linux-file-permissions/)

---

## 👋 About This Portfolio

This repository contains a full set of professional portfolio artifacts aligned with the eight courses of the Google Cybersecurity Professional Certificate. Each project demonstrates practical skills that entry-level **Cybersecurity Analysts** and **SOC Analysts** use daily.

**Target roles:** Cybersecurity Analyst · SOC Analyst · Security Operations · Junior Information Security Analyst

---

## 📜 Certificate Curriculum Coverage

| # | Course | Portfolio Project | Status |
|---|--------|-------------------|--------|
| 1 | Foundations of Cybersecurity | [Professional Statement](./01-professional-statement/) | ✅ Complete |
| 2 | Play It Safe: Manage Security Risks | [Botium Toys Security Audit](./02-botium-toys-security-audit/) | ✅ Complete |
| 3 | Connect and Protect: Networks and Network Security | [Network Security Analysis](./03-network-security-analysis/) | ✅ Complete |
| 4 | Tools of the Trade: Linux and SQL | [Linux Permissions](./04-linux-file-permissions/) + [SQL Queries](./05-sql-security-queries/) | ✅ Complete |
| 5 | Assets, Threats, and Vulnerabilities | [Vulnerability Assessment](./06-vulnerability-assessment/) | ✅ Complete |
| 6 | Sound the Alarm: Detection and Response | [NIST Incident Response](./07-incident-response-nist/) | ✅ Complete |
| 7 | Automate Cybersecurity Tasks with Python | [Python Automation Scripts](./08-python-automation/) | ✅ Complete |
| 8 | Put It to Work: Prepare for Cybersecurity Jobs | This portfolio + career materials | ✅ Complete |

---

## 🗂️ Projects at a Glance

### 01 – Professional Statement
Clear, concise career statement highlighting motivation, transferable skills, and target roles.

### 02 – Botium Toys Internal Security Audit
Full audit package for a fictional retail company:
- Controls assessment (administrative, technical, physical)
- Compliance checklist (PCI DSS, GDPR, SOC)
- Prioritized risk-based recommendations

### 03 – Network Security Analysis
Analysis of network traffic patterns, common attacks (SYN flood, DNS/ICMP anomalies), and hardening recommendations (firewall, segmentation, host hardening).

### 04 – Linux File Permissions
Practical reference for `chmod`, `chown`, permission bits, and least-privilege configurations used in security operations.

### 05 – SQL Security Queries
Ready-to-adapt queries for failed-login detection, date/IP filtering, privileged account activity, and investigation workflows.

### 06 – Vulnerability Assessment
Asset inventory, threat identification, risk scoring (likelihood × impact), and a prioritized remediation plan for a small-business environment.

### 07 – NIST Incident Response
Complete incident handler’s journal aligned with NIST Cybersecurity Framework phases (Detect → Respond → Recover) including timeline and lessons learned.

### 08 – Python Security Automation
Working Python scripts (standard library only):
- `log_parser.py` – detects brute-force / failed-login patterns from auth logs
- `update_file_permissions.py` – demonstrates algorithmic permission decisions
- Includes sample log data for immediate testing

---

## 🛠️ Tools & Technologies Demonstrated

| Category | Tools / Concepts |
|----------|------------------|
| Languages | Python 3, SQL, Bash |
| Operating Systems | Linux (permissions, CLI, logging) |
| Network Analysis | Wireshark / tcpdump concepts, protocol analysis |
| Detection | SIEM concepts (Splunk / Chronicle), IDS (Suricata) |
| Frameworks | NIST CSF, CIA Triad, OWASP principles |
| Compliance Awareness | PCI DSS, GDPR, SOC |
| Soft Skills | Documentation, risk communication, stakeholder recommendations |

---

## 📁 Repository Structure

```
google-cybersecurity-portfolio/
├── index.html                          # GitHub Pages portfolio site
├── README.md                           # This file
├── LICENSE                             # MIT
├── SECURITY.md                         # Security policy
├── .gitignore
├── assets/                             # Certificate image & screenshots
│   └── README.md
├── 01-professional-statement/
│   ├── README.md
│   └── professional-statement.md
├── 02-botium-toys-security-audit/
│   ├── README.md
│   ├── controls-assessment.md
│   ├── compliance-checklist.md
│   └── recommendations.md
├── 03-network-security-analysis/
│   ├── README.md
│   └── network-analysis-report.md
├── 04-linux-file-permissions/
│   ├── README.md
│   └── linux-permissions-guide.md
├── 05-sql-security-queries/
│   ├── README.md
│   └── sql-queries.md
├── 06-vulnerability-assessment/
│   ├── README.md
│   └── vulnerability-report.md
├── 07-incident-response-nist/
│   ├── README.md
│   └── incident-handler-journal.md
└── 08-python-automation/
    ├── README.md
    ├── requirements.txt
    ├── update_file_permissions.py
    ├── log_parser.py
    └── sample_auth.log
```

---


## 🧪 Test the Python Scripts

```bash
cd 08-python-automation

# Run the log parser against the included sample
python3 log_parser.py sample_auth.log

# Run the permissions demo
python3 update_file_permissions.py
```

No external packages required (pure Python standard library).

---

## 📌 Job-Readiness Checklist

- [x] Complete portfolio structure covering all 8 courses
- [x] Working Python automation examples
- [x] Risk, compliance, and incident-response documentation
- [x] Network, Linux, and SQL artifacts
- [x] Replace placeholders with your personal details
- [x] Add official certificate badge / PDF
- [x] Link this repo on LinkedIn and resume
- [x] (Recommended) Prepare for CompTIA Security+ as dual credential

---

## 📄 License

Released under the [MIT License](LICENSE).  
Course scenarios and materials are property of Google / Coursera and are used here solely for educational portfolio purposes.

---

