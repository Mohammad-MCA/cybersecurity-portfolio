# SQL Queries for Security Analysis

## Basic Filtering Examples

### Find failed login attempts
```sql
SELECT username, ip_address, timestamp, status
FROM login_attempts
WHERE status = 'failed'
ORDER BY timestamp DESC;
```

### Filter by date range
```sql
SELECT *
FROM access_logs
WHERE timestamp BETWEEN '2025-09-01' AND '2025-09-30'
  AND status_code >= 400;
```

### Search for suspicious patterns
```sql
SELECT username, COUNT(*) AS fail_count
FROM login_attempts
WHERE status = 'failed'
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY username
HAVING COUNT(*) > 5
ORDER BY fail_count DESC;
```

### Filter by IP address or range
```sql
SELECT *
FROM network_logs
WHERE source_ip LIKE '192.168.1.%'
   OR source_ip IN ('10.0.0.15', '10.0.0.22');
```

### Find privileged account activity
```sql
SELECT user_id, action, resource, timestamp
FROM audit_log
WHERE user_id IN (
    SELECT user_id FROM users WHERE role = 'admin'
)
ORDER BY timestamp DESC
LIMIT 100;
```

## Security Best Practices When Querying

1. **Least privilege** – Use a read-only database account for analysis whenever possible.  
2. **Avoid SELECT *** on sensitive tables in production – Request only needed columns.  
3. **Be careful with LIKE patterns** – Leading wildcards (`%value`) can be slow; prefer exact or trailing matches when feasible.  
4. **Protect query results** – Treat exported query output as sensitive data.  
5. **Log your own queries** – Maintain an audit trail of investigations.

## Sample Investigation Workflow

1. Identify the time window of the suspected incident.  
2. Query authentication and access logs for that window.  
3. Aggregate by user / IP to surface outliers.  
4. Pivot to related tables (file access, process execution, network connections).  
5. Document findings and escalate according to the incident response plan.

---

