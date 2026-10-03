> **⚠️Spoiler Warning:** This documentation contains solutions and methodology for the Blue Team Labs Online (BTLO) challenge "The Report". 

# BTLO Challenge: The Report
**Platform:** Blue Team Labs Online  
**Category:** Security Operations / Threat Intelligence  
**Difficulty:** Easy  

## Overview
This challenge focused on extracting actionable threat intelligence from the 2022 Red Canary Threat Detection Report. The objective was to parse a comprehensive industry document to identify specific Indicators of Compromise (IOCs), threat actor behaviors, and detection engineering rules.

## Tools & Environment
*   **Hardware:** Apple MacBook Neo
*   **Software/Tools:** Native PDF Reader, Targeted Keyword Search (Cmd + F)
*   **Methodology:** Targeted reading and OSINT extraction techniques

## Investigation Walkthrough & Methodology

*Note: Below is a breakdown of the analytical process used to extract the required intelligence.*

### Identifying Software Vulnerabilities
To find the specific Java logging library mentioned in the 2021 context, I utilized the document's structure and targeted search queries for "Java logging" and "2021". This led directly to the section detailing the exploitation of **Log4j**, a critical vulnerability that affected numerous enterprise environments.

### Tracing Threat Actor Infrastructure
When tasked with identifying the two outdated software platforms targeted by coin miners, I scanned the threat landscape sections for keywords like "coin miners" and "outdated". The report highlighted that adversaries frequently scan for unpatched instances of **JBoss,WebLogic** to deploy cryptocurrency mining payloads.

### Understanding Execution Vectors
To determine the parent process associated with malicious JavaScript files, I navigated to the detection engineering section. By reviewing the detection rules for script execution, I confirmed that adversaries rely on **wscript.exe** to run malicious scripts outside of standard browser environments.

## Key Takeaways
*   **Threat Intelligence Parsing:** Developed the ability to rapidly skim and extract specific IOCs from a 100+ page technical document.
*   **Detection Engineering Context:** Gained insight into how threat reports map adversary behaviors to specific detection rules (e.g., monitoring `wscript.exe` execution).
*   **Efficiency:** Practiced targeted keyword searching rather than cover-to-cover reading, mirroring the time-sensitive intelligence gathering required in a SOC environment.
