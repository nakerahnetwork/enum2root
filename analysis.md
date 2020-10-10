## nmap
```
nmap -T5 --open -sSU --min-rate=1000 --max-retries=2 -p- $ip 
```
**Result:**
```
Nmap done: 1 IP address (1 host up) scanned in 393.57 seconds
```
---
```
nmap -p- -T5 $ip
```
**Result:**
```
Nmap done: 1 IP address (1 host up) scanned in 900.15 seconds
```
---

