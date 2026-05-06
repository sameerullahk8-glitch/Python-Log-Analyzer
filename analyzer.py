failed_attempts = {}

# Open log file
with open("log.txt", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-1]  # last part is IP
            
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("=== Suspicious Activity Report ===\n")

for ip, count in failed_attempts.items():
    print(f"IP: {ip} | Failed Attempts: {count}")
    
    if count >= 3:
        print(f"⚠️ ALERT: Possible brute-force attack from {ip}\n")