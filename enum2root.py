#!/usr/bin/python3
import subprocess, sys

def nmapBasic(IP):
    scan = subprocess.run("nmap -sC -sV -T4 -oN nmapbasic.log {} ".format(IP), capture_output = True, shell = True)
    out = scan.stdout.decode()
    return out


def nmapFullPort(IP):
    scan = subprocess.run("nmap -p- -T4 -oN nmapfull.log {}".format(IP), capture_output = True, shell = True)
    out = scan.stdout.decode()
    return out

def gobusterBasic(IP, WORDLIST):
    scan = subprocess.run("gobuster dir -u http://{} -w {} -t 35 -x txt,php -o dirbasic.log".format(IP,WORDLIST), capture_output = True, shell = True)
    out = scan.stdout.decode()
    return out

def basicEnum(IP, WORDLIST):
    nmapBasic(IP)
    nmapFullPort(IP)
    gobusterBasic(IP, WORDLIST)

basicEnum(sys.argv[1], sys.argv[2])
