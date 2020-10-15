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
- gobuster with your specified wordlist (-x txt)

### To-Do:
- [x] full port scan with service detection
- [ ] get services details and docs from the internet (ippsec.rocks)
	- [ ] FTP + Anonymous login --> get files
	- [ ] Spider port 80 for dns name
- [ ] [get vulns with CVE data using searchsploit](https://pypi.org/project/getsploit/), [or this](https://github.com/OCSAF/freevulnsearch)
- [ ] concurrency using threading/multiprocessing
