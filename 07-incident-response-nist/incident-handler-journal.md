# Incident Handler’s Journal 

**Incident ID:** INC-2025-0915-001  
**Date Opened:** 2025-09-15  
**Handler:** Mohammad  
**Severity:** High  

---

## 1. Detection (Detect)

- **Source of alert:** SIEM correlation rule – multiple failed logins followed by successful login from unusual geographic location.  
- **Time of detection:** 2025-09-15 09:14 UTC  
- **Initial indicators:**  
  - 47 failed login attempts in 8 minutes for user `j.smith`  
  - Successful login from IP geolocated outside normal working region  
  - Subsequent access to sensitive file share  

## 2. Analysis & Containment (Respond)

- Account `j.smith` temporarily disabled.  
- Source IP blocked at perimeter firewall.  
- Endpoint isolation request sent to desktop support for the user’s workstation.  
- Relevant logs exported and stored in evidence folder (read-only).  

**Timeline (UTC):**  
| Time | Action |  
|------|--------|  
| 09:14 | Alert received |  
| 09:18 | Account locked |  
| 09:22 | IP blocked |  
| 09:35 | Endpoint isolated |  
| 10:05 | Initial stakeholder notification sent |  

## 3. Eradication & Recovery (Respond / Recover)

- Password reset and MFA re-enrollment required for the affected account.  
- Full antivirus / EDR scan of the endpoint completed – no malware found.  
- Review of recent file access showed no large data exfiltration.  
- Account re-enabled after confirmation with the user and manager.  

## 4. Lessons Learned / Post-Incident (Identify / Protect improvements)

- Recommendation: Implement geo-velocity and impossible-travel detections in SIEM.  
- Recommendation: Reduce lockout threshold and add progressive delays.  
- Recommendation: Ensure all privileged accounts have MFA enforced.  
- Update playbook with improved communication template for similar incidents.  

## 5. Status

**Closed** – 2025-09-16  

---

