#!/usr/bin/python3
import subprocess, sys
import xml.etree.ElementTree as ET
from pathlib import Path
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S')

##prep##
def mkdirs():
    Path("nmap/basic").mkdir(parents=True, exist_ok=True)
    Path("nmap/full").mkdir(parents=True, exist_ok=True)

##nmap##
def nmapBasicDetailed(IP):
    mkdirs()
    logging.info("Initiating Basic Detailed nmap Scan")
    scan = subprocess.run("nmap -sC -sV -T4 -oA  nmap/basic/fast {} ".format(IP), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    out = scan.stdout.decode()
    return out

def nmapFullBasic(IP):
    mkdirs()
    logging.info("Initiating Full Basic Scan")
    scan = subprocess.run("nmap -p- -T5 --open -sSU --min-rate=1000 --max-retries=2 -oA nmap/full/fast {}".format(IP), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    out = scan.stdout.decode()
    return out

def nmapFullDetailed(IP):
    mkdirs()
    nmapFullBasic(IP)
    logging.info("Initiating Full Detailed Scan")
    ports = ",".join(parseXMLnmap("nmap/full/fast.xml"))
    scan = subprocess.run("nmap -p {} -sC -sV -T4 -oA nmap/full/detailed {} ".format(ports, IP), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    out = scan.stdout.decode()
    return out

def parseXMLnmap(file):
    logging.info("parsing XML files")
    tree = ET.parse("{}".format(file))
    root = tree.getroot()
    ports = [port.get('portid') for port in root.findall('.//port')]
    return ports
##Gobuster##
def gobusterBasic(IP, WORDLIST):
    scan = subprocess.run("gobuster dir -u http://{} -w {} -t 35 -x txt,php -o dirbasic.log".format(IP,WORDLIST), capture_output = True, shell = True)
    out = scan.stdout.decode()
    return out

def basicEnum(IP, WORDLIST):
    nmapBasicDetailed(IP)
    nmapFullBasic(IP)
    gobusterBasic(IP, WORDLIST)

def detailedEnum(IP, WORDLIST):
    nmapFullDetailed(IP)
    gobusterBasic(IP, WORDLIST)

#basicEnum(sys.argv[1], sys.argv[2])
detailedEnum(sys.argv[1], sys.argv[2])

