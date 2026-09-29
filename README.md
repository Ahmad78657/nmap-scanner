# nmap-scanner

A minimal Python CLI that wraps `nmap -sn` (ping sweep) to find live
hosts on a subnet and produce a readable report.

## Requirements

- Python 3.8+
- `nmap` installed (`sudo apt install nmap`)

## Usage

```bash
python3 scanner.py 192.168.1.0/24
python3 scanner.py 192.168.1.0/24 -o report.txt
```

## Example output

```
[*] Scanning 192.168.1.0/24 ... (this may take a minute)

Nmap Scanner Report
Target : 192.168.1.0/24
Time   : 2026-09-29T12:34:56
Hosts  : 4 alive
----------------------------------------
  • 192.168.1.1
  • 192.168.1.10
  • 192.168.1.42
  • 192.168.1.100
```

## Why

Built as a learning project to practice `argparse`, `subprocess`,
and parsing text output — plus a bit of network reconnaissance.
