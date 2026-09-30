# Network Security Analysis Report

## 1. Purpose

This report summarizes analysis of network traffic patterns and hardening recommendations performed as part of the Google Cybersecurity Professional Certificate (Course 3).

## 2. Key Concepts Reviewed

- **OSI / TCP-IP model** – Understanding where protocols and attacks operate  
- **Common protocols** – TCP, UDP, ICMP, DNS, HTTP/HTTPS  
- **Attack examples** – SYN flood (DoS), DNS spoofing / amplification, ICMP-based reconnaissance  
- **Hardening techniques** – Firewall rules, disabling unnecessary services, network segmentation, secure configurations

## 3. Sample Findings (Illustrative)

### Suspicious Traffic Indicators

| Indicator | Possible Meaning | Recommended Action |
|-----------|------------------|--------------------|
| High volume of SYN packets to a single host | Possible SYN flood / DoS | Rate-limit SYN packets, enable SYN cookies, investigate source |
| Unusual DNS queries (long domain names, high frequency) | Possible tunneling or C2 | Inspect DNS logs, block suspicious domains |
| ICMP echo requests from external sources | Reconnaissance | Restrict ICMP at the perimeter where appropriate |
| Connections to known malicious IPs | Compromised host or scanning | Block at firewall, isolate host, investigate |

### Hardening Recommendations

1. **Firewall**  
   - Default-deny inbound rules  
   - Allow only required ports (e.g., 443, 22 from trusted sources)  
   - Log and review denied traffic

2. **Network Segmentation**  
   - Separate guest, employee, and server networks  
   - Place public-facing services in a DMZ

3. **Host Hardening**  
   - Disable unused services and ports  
   - Keep systems patched  
   - Enforce strong authentication (SSH keys + MFA where possible)

4. **Monitoring**  
   - Capture baseline traffic patterns  
   - Use IDS (Suricata) or SIEM alerts for anomalies

## 4. Conclusion

Understanding normal vs. anomalous network behavior is foundational for detection and response. Combining packet analysis skills with systematic hardening significantly reduces the attack surface.

---

*Replace the illustrative findings above with screenshots and analysis from your actual course labs (Wireshark filters, tcpdump output, etc.).*
