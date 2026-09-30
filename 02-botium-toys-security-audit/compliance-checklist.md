# Compliance Checklist – Botium Toys

## PCI DSS (Payment Card Industry Data Security Standard)

| Requirement Area | Status | Gap Notes |
|------------------|--------|-----------|
| Build and maintain a secure network (firewalls) | Partial | Firewall present but rules not formally reviewed |
| Protect cardholder data (encryption) | Fail | No encryption of stored cardholder data |
| Maintain vulnerability management program | Partial | Ad-hoc patching only |
| Implement strong access control measures | Fail | No least privilege or MFA |
| Regularly monitor and test networks | Fail | No IDS, limited logging |
| Maintain information security policy | Partial | Policies exist but incomplete |

**Overall PCI DSS posture:** Significant gaps — high risk if cardholder data is stored or processed.

## GDPR (General Data Protection Regulation)

| Principle / Requirement | Status | Gap Notes |
|-------------------------|--------|-----------|
| Lawfulness, fairness, transparency | Partial | Privacy notice exists but limited |
| Purpose limitation & data minimization | Partial | Data retention policy unclear |
| Integrity and confidentiality (security) | Fail | Missing encryption and access controls |
| Accountability | Partial | Limited documentation of processing activities |
| Breach notification readiness | Fail | No incident response or notification process |

**Overall GDPR posture:** Not ready for EU customer data without major improvements.

## SOC (System and Organization Controls)

| Area | Status | Gap Notes |
|------|--------|-----------|
| Security | Partial | Basic technical controls present |
| Availability | Fail | No formal backup / DR plan |
| Confidentiality | Fail | Missing encryption and strong access control |
| Processing integrity | Partial | Limited monitoring |
| Privacy | Partial | Incomplete policies |

**Overall SOC readiness:** Not currently prepared for a SOC 2 examination.

---

*Update this checklist with the exact findings from your course activity.*
