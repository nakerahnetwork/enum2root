## Still Work in Progress

### Requirements:
- **Python3.8**

### Usage:
```bash
python3 enum2root.py [IP] [Wordlist]
```
### Info:
script will run and produces logs with the output the following:
	- nmap basic scan (-sC -sV)
	- nmap full port scan (-p-)
	- gobuster with your specified wordlist (-x txt,php)
