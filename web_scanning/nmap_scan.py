# Simple Nmap scan script
import os

target = input("Enter target IP or domain: ")
print(f"Scanning {target} ...")
os.system(f"nmap -sV -T4 {target}")
