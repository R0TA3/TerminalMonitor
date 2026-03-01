# TerminalMonitor

**TerminalMonitor** is a Python-based monitoring tool for Linux systems that provides **real-time system log tracking and network traffic monitoring**. This tool is designed for system administrators, network analysts, and anyone learning cybersecurity or system monitoring in an ethical environment.  

> ⚠️ **Important:** Network sniffing requires root privileges. Always use this tool on systems you are authorized to monitor.

---

## Features

- **System Log Monitoring**
  - Observes `/var/log/boot.log` and `/var/log/dpkg.log`.
  - Real-time updates of system boot events and package activity.

- **Network Monitoring**
  - Captures live network packets using **Scapy**.
  - Displays packet details (source, destination, protocol, etc.).
  - Requires elevated privileges for raw socket access.

- **Modular Design**
  - `main.py` – entry point.
  - `system_monitor.py` – system log monitoring module.
  - `network_monitor.py` – network sniffing module.
  - `database.py` – optional storage backend.
  - `models.py` – data structures and models.

- **Cross-Platform Python Support**
  - Compatible with Python 3.13+ on Linux.
  - Uses virtual environment (`venv`) for dependency management.

---

## Installation

1. **Clone the repository**

```bash
git clone git@github.com:R0TA3/TerminalMonitor.git
cd TerminalMonitor

Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Note: If requirements.txt does not exist, install manually:
pip install scapy

Usage

Run the tool (requires root for network sniffing):

sudo python3 main.py

Example output:

Monitoring /var/log/boot.log ...
Monitoring /var/log/dpkg.log ...
System log monitoring started...
Network monitoring started...
Packet captured: [source IP → destination IP, protocol, etc.]
Troubleshooting

PermissionError on network monitoring
Ensure you run the script with sudo or give Python raw socket capabilities:

sudo setcap cap_net_raw,cap_net_admin=eip $(which python3)

Python module errors
Activate the virtual environment and install dependencies.

Security & Ethics

Only use on systems you own or are authorized to monitor.

Capturing traffic on networks without permission is illegal.

TerminalMonitor is intended for educational and ethical purposes.

Future Enhancements

Logging network traffic to a database.

Alerting for suspicious activity.

Web-based dashboard for monitoring.

Advanced network protocol filtering.

License

This project is open-source. Feel free to fork, modify, and use ethically.

Author

ROTA3 – Linux & Cybersecurity Enthusiast
Email: www.achua6@gmail.com

GitHub: https://github.com/R0TA3


---

💡 **Next step:**  

1. Save this as `README.md` in your `TerminalMonitor` folder:  

```bash
nano README.md
# Paste the content and save

Commit and push:

git add README.md
git commit -m "Add professional README"
git push

Your GitHub repository will now look polished, professional, and ready for presentation.
