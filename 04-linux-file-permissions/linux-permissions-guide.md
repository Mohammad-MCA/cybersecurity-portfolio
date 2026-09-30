# Linux File Permissions – Practical Guide

## Viewing Permissions

```bash
ls -l                  # long listing with permissions
ls -la                 # include hidden files
stat filename          # detailed file metadata
```

Example output:
```
-rw-r--r-- 1 alice analysts 4096 Oct 1 10:00 report.txt
```

| Position | Meaning |
|----------|---------|
| 1        | File type (`-` regular, `d` directory, `l` link) |
| 2-4      | Owner permissions (rwx) |
| 5-7      | Group permissions |
| 8-10     | Others permissions |

## Changing Permissions with `chmod`

### Symbolic mode
```bash
chmod u+x script.sh          # add execute for owner
chmod g-w file.txt           # remove write for group
chmod o=r file.txt           # set others to read-only
chmod u=rwx,g=rx,o= file     # explicit setting
```

### Numeric (octal) mode
```bash
chmod 755 script.sh          # rwxr-xr-x
chmod 640 secrets.txt        # rw-r-----
chmod 700 private_dir        # rwx------
```

Common secure values:
- `600` – owner read/write only (private files)
- `640` – owner read/write, group read
- `700` – owner full access only (directories/scripts)
- `750` – owner full, group read/execute

## Changing Ownership

```bash
chown alice file.txt              # change owner
chown alice:analysts file.txt     # change owner and group
chgrp analysts file.txt           # change group only
```

## Best Practices for Security

1. **Least privilege** – Grant only the permissions required for the role.  
2. **Avoid world-writable files** – Especially scripts and configuration files.  
3. **Protect sensitive data** – Use `600` or `640` for credentials, logs containing PII, etc.  
4. **Directories** – Execute bit is required to enter a directory; plan carefully.  
5. **umask** – Set a restrictive default umask (e.g., `027` or `077`) for new files.  
6. **Regular audits** – Periodically review permissions on critical paths (`/etc`, `/var/log`, application directories).

## Sample Security Scenario

A log directory should be readable by the security team but writable only by the logging service:

```bash
chown root:security /var/log/app
chmod 750 /var/log/app
chmod 640 /var/log/app/*.log
```

---

*Add your own command history, screenshots, or course lab outputs here.*
