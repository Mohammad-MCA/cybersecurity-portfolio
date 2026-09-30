#!/usr/bin/env python3
"""
log_parser.py
-------------
Simple authentication log parser for detecting failed login attempts.
Inspired by Google Cybersecurity Certificate Python automation labs.

Usage:
  python3 log_parser.py <logfile>
  python3 log_parser.py sample_auth.log
"""

import sys
import re
from collections import defaultdict
from datetime import datetime


# Common pattern for Linux auth.log style lines containing "Failed password"
FAILED_PATTERN = re.compile(
    r"(?P<timestamp>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*"
    r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)


def parse_log(filepath: str) -> dict:
    """
    Parse the log file and return a dictionary of
    {ip: {"count": n, "users": set(), "first": ts, "last": ts}}
    """
    results = defaultdict(lambda: {"count": 0, "users": set(), "first": None, "last": None})

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                match = FAILED_PATTERN.search(line)
                if not match:
                    continue

                ip = match.group("ip")
                user = match.group("user")
                ts = match.group("timestamp")

                entry = results[ip]
                entry["count"] += 1
                entry["users"].add(user)
                if entry["first"] is None:
                    entry["first"] = ts
                entry["last"] = ts

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    return results


def print_report(results: dict, threshold: int = 5) -> None:
    """Print a summary of IPs that exceeded the failed-login threshold."""
    print("Failed Login Summary")
    print("=" * 60)

    suspicious = {ip: data for ip, data in results.items() if data["count"] >= threshold}

    if not suspicious:
        print(f"No IPs exceeded the threshold of {threshold} failed attempts.")
        return

    for ip, data in sorted(suspicious.items(), key=lambda x: x[1]["count"], reverse=True):
        users = ", ".join(sorted(data["users"]))
        print(f"IP: {ip}")
        print(f"  Failed attempts : {data['count']}")
        print(f"  Targeted users  : {users}")
        print(f"  First seen      : {data['first']}")
        print(f"  Last seen       : {data['last']}")
        print("-" * 40)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 log_parser.py <logfile>")
        print("\n--- Demo mode (no file provided) ---")
        # Synthetic demo data
        demo_results = {
            "203.0.113.45": {
                "count": 12,
                "users": {"admin", "root", "j.smith"},
                "first": "Sep 15 08:01:12",
                "last": "Sep 15 08:09:44",
            },
            "198.51.100.22": {
                "count": 7,
                "users": {"guest"},
                "first": "Sep 15 09:15:03",
                "last": "Sep 15 09:18:21",
            },
        }
        print_report(demo_results)
        return

    logfile = sys.argv[1]
    results = parse_log(logfile)
    print_report(results)


if __name__ == "__main__":
    main()
