#!/usr/bin/python3
import nmap3
import subprocess
import sys
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

##masscan##
def masscanFull(IP):
    logging.info("Scanning all ports with masscan")
    scan = subprocess.run("masscan -p1-65535,U:1-65535 {} --rate=1000 -oX -".format(IP), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    out = scan.stdout.decode()
    return out

def nmapFullDetailed(IP,ports):
    logging.info("Starting a detailed nmap scan with masscan results")
    scan = nmap.nmap_version_detection("10.10.41.38", args="-sC -T5 --min-rate=1000 --max-retries=2")
    #scan = subprocess.run("nmap -p {} -sC -sV -T4 -oA ports.log {} ".format(ports, IP), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    out = scan.stdout.decode()
    return out

def parseXML(XML):
    logging.info("parsing XML files")
    #tree = ET.parse("{}".format(file))
    tree = ET.ElementTree(ET.fromstring(XML))
    root = tree.getroot()
    ports = [port.get('portid') for port in root.findall('.//port')]
    ports_string = ",".join(ports)
    return ports_string

def basicEnum(IP, WORDLIST):
    nmapBasicDetailed(IP)
    nmapFullBasic(IP)
    gobusterBasic(IP, WORDLIST)

def detailedEnum(IP):
    scan = masscanFull(IP)
    ports = parseXML(scan)
    final = nmapFullDetailed(IP,ports)
    return final
#basicEnum(sys.argv[1], sys.argv[2])
#print(detailedEnum(sys.argv[1]))

