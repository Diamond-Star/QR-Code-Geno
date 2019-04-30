"""
InstallPkg.py
This file is used once by the program at the first time to check and install
Python pacjages required by the program.
"""
import os

print("---- Welcome to QRCode Geno ----",
	"Packages setup is taking place.",
	"This process requires interner connection.",
	"This would take a few minutes.", sep = "\n")

# Run pip by OS system shell command.
myCmd = 'pip install -r requirements.txt'
os.system(myCmd)
