> **⚠️Spoiler Warning:** This documentation contains solutions and methodology for the Blue Team Labs Online (BTLO) challenge "Phishing Analysis". 

# BTLO Challenge: Phishing Analysis
**Platform:** Blue Team Labs Online  
**Category:** Security Operations / Phishing  
**Difficulty:** Easy  

## Overview
This challenge involved analyzing raw email artifacts from a simulated phishing campaign. The objective was to safely handle malicious `.eml` files, parse email headers, and extract key Indicators of Compromise (IOCs) without executing the payloads. 
Successfully identified a multi-stage phishing campaign utilizing URL redirection to bypass automated scanners.

## Tools & Environment
*   **Hardware:** Apple MacBook Neo
*   **Software/Tools:** TextEdit (Raw header analysis), DomainTools (Reverse DNS), URL2PNG (Safe URL rendering)
*   **Methodology:** Static analysis, OSINT, Header parsing

## Investigation Walkthrough & Methodology

### 1. Safe Artifact Handling & Initial Triage
To prevent accidental execution of embedded tracking pixels or malicious links, I avoided opening the evidence in a native mail client. Instead, I opened the `Website contact form submission.eml` file directly in a text editor to analyze the raw code and headers safely. The primary recipient was immediately visible in the `To:` field.

### 2. Identifying the Originating Infrastructure
By analyzing the bottom-most `Received` headers and searching for `X-Sender-IP`, I identified the true originating IP address of the sender as **103.9.171.10**. I then performed a reverse DNS lookup using DomainTools, resolving the malicious IP to the host `c5s2-1e-syd.hosting-services.net.au`.

### 3. Payload Extraction & Link Obfuscation
Scrolling to the `Content-Disposition` section of the headers, I located the malicious nested attachment. Inside, I found an obfuscated URL string that stitched two separate domains together (`hxxps://35000usdperwwekpodf.blogspot.sg?p=9swg` leading to a `.co.il` domain). This is a common evasion technique designed to bypass automated security scanners via URL redirection.

### 4. Safe Payload Detonation
Instead of clicking the extracted URL, I utilized **URL2PNG** to safely capture a server-side screenshot of the destination page. The resulting image confirmed the malicious Blogspot infrastructure had already been reported and taken down, displaying a "Blog has been removed" error.

## Key Takeaways
*   **Artifact Safety:** Gained practical experience handling and inspecting `.eml` files without triggering malicious execution.
*   **Header Parsing:** Practiced manual extraction of routing data and originating IP addresses directly from email headers to bypass spoofed sender addresses.
*   **OSINT Integration:** Leveraged third-party intelligence and sandboxing tools to safely investigate active malicious infrastructure.
