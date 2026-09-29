
import argparse
import subprocess
import sys
import re
from datetime import datetime


def run_nmap(target: str) -> str:
    """Run nmap -sn (ping sweep) and return raw stdout."""
    try:
        result = subprocess.run(
            ["nmap", "-sn", target],
            capture_output=True,
            text=True,
            timeout=300,
        )
        if result.returncode != 0:
            print(f"[!] nmap error:\n{result.stderr}", file=sys.stderr)
            sys.exit(1)
        return result.stdout
    except FileNotFoundError:
        print("[!] nmap not found. Install it: sudo apt install nmap", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("[!] nmap timed out.", file=sys.stderr)
        sys.exit(1)


def parse_hosts(raw: str) -> list[str]:
    """Extract 'Nmap scan report for <host>' lines."""
    hosts = re.findall(r"Nmap scan report for (.+)", raw)
    return [h.strip() for h in hosts]


def main():
    parser = argparse.ArgumentParser(
        description="Scan a subnet for live hosts using nmap.",
    )
    parser.add_argument("target", help="Target, e.g. 192.168.1.0/24")
    parser.add_argument("-o", "--output", help="Write report to a file")
    args = parser.parse_args()

    print(f"[*] Scanning {args.target} ... (this may take a minute)")
    raw = run_nmap(args.target)
    hosts = parse_hosts(raw)

    lines = [
        f"Nmap Scanner Report",
        f"Target : {args.target}",
        f"Time   : {datetime.now().isoformat(timespec='seconds')}",
        f"Hosts  : {len(hosts)} alive",
        "-" * 40,
    ]
    lines += [f"  • {h}" for h in hosts] if hosts else ["  (no live hosts found)"]
    report = "\n".join(lines)

    print()
    print(report)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report + "\n")
        print(f"\n[+] Report saved to {args.output}")


if __name__ == "__main__":
    main()

