# Python Log Analyzer

## Objective
Detect suspicious login attempts from system logs.

## Tools Used
- Python

## Features
- Detects failed login attempts
- Identifies suspicious IP addresses
- Flags possible brute-force attacks

## How It Works
The script reads a log file and counts failed login attempts per IP address. If attempts exceed a threshold, it flags the IP as suspicious.

## Example Output
IP: 192.168.1.10 | Failed Attempts: 4  
ALERT: Possible brute-force attack  

## What I Learned
- Log analysis techniques
- Detecting brute-force attacks
- Basic security automation
