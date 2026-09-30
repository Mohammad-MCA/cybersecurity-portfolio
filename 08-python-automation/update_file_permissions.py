#!/usr/bin/env python3
"""
update_file_permissions.py
--------------------------
Sample script inspired by the Google Cybersecurity Certificate
"Automate Cybersecurity Tasks with Python" course.

Purpose:
  Demonstrate a simple algorithm that processes a list of files
  and applies permission-related decisions based on file type
  or naming conventions.

Note:
  This is an educational example. In a real environment you would
  use the `os` and `stat` modules (or subprocess calls to chmod/chown)
  with proper error handling and least-privilege considerations.
"""

import os
from pathlib import Path

# Example policy rules (customize as needed)
PERMISSION_POLICY = {
    ".log": "640",      # owner rw, group r
    ".conf": "600",     # owner only
    ".sh": "750",       # owner rwx, group rx
    ".key": "600",      # private keys
    "default": "644",
}


def get_recommended_mode(filename: str) -> str:
    """Return a recommended octal permission string based on extension."""
    ext = Path(filename).suffix.lower()
    return PERMISSION_POLICY.get(ext, PERMISSION_POLICY["default"])


def process_files(file_list: list[str]) -> None:
    """
    Process each file and print the recommended permission change.
    In a real script this would call os.chmod().
    """
    print("File Permission Update Report")
    print("=" * 50)

    for filepath in file_list:
        if not os.path.exists(filepath):
            print(f"[SKIP] {filepath} – file not found")
            continue

        recommended = get_recommended_mode(filepath)
        current = oct(os.stat(filepath).st_mode)[-3:]  # last 3 digits

        if current == recommended:
            status = "OK"
        else:
            status = f"CHANGE {current} → {recommended}"

        print(f"{filepath:<40} {status}")


def main():
    # Example file list – replace with actual paths or directory walk
    sample_files = [
        "/var/log/auth.log",
        "/etc/ssh/sshd_config",
        "/opt/scripts/backup.sh",
        "/home/analyst/.ssh/id_rsa",
        "report.txt",
    ]

    # For demonstration we only process files that exist on this system
    existing = [f for f in sample_files if os.path.exists(f)]
    if not existing:
        print("No sample files found on this system.")
        print("Add real paths to sample_files or pass a directory to walk.")
        # Demo output with fictional data
        print("\n--- Demo Output ---")
        demo = [
            ("auth.log", "640"),
            ("sshd_config", "600"),
            ("backup.sh", "750"),
            ("id_rsa", "600"),
            ("report.txt", "644"),
        ]
        for name, mode in demo:
            print(f"{name:<30} recommended mode: {mode}")
        return

    process_files(existing)


if __name__ == "__main__":
    main()
