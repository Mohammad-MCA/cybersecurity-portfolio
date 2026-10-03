# BTLO Write-Up: Network Analysis - Ransomware
**Analyst:** Mohammad
**Date:** October 2026

> [!WARNING]
> **SPOILER warning:** This document contains a full walkthrough, indicators of compromise, and the final solution flag for the Blue Team Labs Online (BTLO) "Network Analysis - Ransomware" challenge. If you are currently attempting the lab, turn back now!
> 
## Executive Summary
This report details the investigation of a network traffic capture (`.pcapng`) involving a suspected ransomware infection. The objective was to analyze the network traffic, identify the malicious payload, determine the ransomware family, and successfully decrypt a compromised tender document.

## Analyst Environment & Tools
* **Host System:** Apple MacBook Neo (8 GB RAM)
* **Translation Layer:** Whisky (for Windows `.exe` execution)
* **Analysis Tools:** Wireshark, macOS Terminal, VirusTotal, TeslaDecoder

## Investigation & Findings

### 1. Infected Host Identification
* **Objective:** Determine the operating system of the compromised machine.
* **Method:** Analyzed the `ransom_traffic.pcapng` file metadata in Wireshark (`Statistics` > `Capture File Properties`).
* **Finding:** The infected host was running **32-bit Windows 7 Service Pack 1, build 7601**.

### 2. Payload Delivery Analysis
* **Objective:** Trace the exact URL used to download the ransomware payload.
* **Method:** Applied the Wireshark display filter `http.request` to isolate outgoing web requests. Identified a `GET` request originating from the infected host (`10.0.2.15`) pointing to an executable file.
* **Finding:** The ransomware was downloaded from `http://10.0.2.15:8000/safecrypt.exe`. The executable file was named **safecrypt.exe**.

### 3. Malware Identification & Threat Intelligence
* **Objective:** Extract the malware and verify its identity via threat intelligence.
* **Method:** 
  1. Extracted the payload from the pcap using Wireshark (`File` > `Export Objects` > `HTTP`).
  2. Calculated the file hash via the macOS terminal using the `md5` command.
  3. Cross-referenced the hash on VirusTotal.
* **Finding:** 
  * **MD5 Hash:** `4a1d88603b1007825a9c6b36d1e5de44`.
  * **Ransomware Family:** The hash is universally identified as **TeslaCrypt**.

### 4. Encryption & Command and Control (C2)
* **Objective:** Identify the encryption algorithm and the associated C2 infrastructure.
* **Method:** Reviewed the provided ransom note and pivoted from the VirusTotal hash report to the "Relations" tab to find contacted domains.
* **Finding:** 
  * **Encryption Algorithm:** RSA-4096 (as stated in the attacker's ransom note).
  * **C2 Domain:** `dunyamuzelerimuzesi.com`.

## Remediation & Decryption
* **Objective:** Recover the encrypted `.micro` tender document.
* **Method:** Utilized **TeslaDecoder** (by BloodDolly), a known decryption tool for the TeslaCrypt family. Ran the Windows executable via a Whisky bottle on macOS to decrypt the target file.
* **Result:** The document was successfully restored to its original `.pdf` format, revealing the final flag: `BTLO-T3nd3r-Fl@g`.
