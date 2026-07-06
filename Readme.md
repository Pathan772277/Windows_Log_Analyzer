# 🛡️ Windows Event Log Analyzer

A Python-based Windows Event Log Analyzer built for SOC (Security Operations Center) and Blue Team learning. This project analyzes exported Windows Security Event Logs in CSV format and generates a simple security report.

## 📌 Features

- Read Windows Security Event Log CSV files
- Count successful logons (Event ID 4624)
- Count failed logons (Event ID 4625)
- Count new user accounts (Event ID 4720)
- Count deleted user accounts (Event ID 4726)
- Detect administrator privilege events (Event ID 4672)
- Detect Security Log Cleared events (Event ID 1102)
- Count failed login attempts per user
- Generate a Windows Security Report

---

## 📂 Project Structure

```
Windows-Event-Analyzer/
│
├── analyzer.py
├── security_log.csv
└── Readme.md
```

---

## 🛠 Technologies Used

- Python 3
- CSV File Handling
- Dictionaries
- Loops
- Conditional Statements
- Windows Security Event IDs

---

## 📊 Event IDs Used

| Event ID | Description |
|----------|-------------|
| 4624 | Successful Logon |
| 4625 | Failed Logon |
| 4672 | Special Privileges Assigned |
| 4720 | User Account Created |
| 4726 | User Account Deleted |
| 1102 | Security Log Cleared |

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Windows-Event-Analyzer.git
```

Go to the project directory:

```bash
cd Windows-Event-Analyzer
```

Run the analyzer:

```bash
python analyzer.py
```

---

## 📋 Sample Output

```
======================================
     WINDOWS SECURITY REPORT
======================================

Successful Logons : 3
Failed Logons     : 3
New Users         : 1
Deleted Users     : 1
Admin Events      : 1
Security Log Cleared : YES

Failed Login Users
------------------
Administrator -> 2
Guest -> 1
```

---

## 🎯 Learning Objectives

This project helped me learn:

- Windows Security Event IDs
- CSV file processing in Python
- Log analysis
- Security event monitoring
- Dictionary-based counting
- Basic SOC automation
- Report generation

---

## 🚀 Future Improvements

- Parse real Windows `.evtx` files
- Export reports to TXT/PDF
- Filter events by date and time
- Sort failed users by count
- Detect suspicious login patterns
- Add command-line arguments
- Improve error handling

---

## 👨‍💻 Author

**Pathan Nafil F**


Aspiring SOC Analyst | Blue Team Learner