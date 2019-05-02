A simple GUI project based on Python 3 with the scope to generate a QR Code.

# Author: 
Waseem S. (Nickname: Diamond Star).

# About:
 - QR Code Geno is a simple program written in Python 3.7.2
 - Its purpose is to generats a QR code for a text supplied by the user, 
that could be captured by a phone camera or so for using in various apps that support QR code.

# Limitation:
 - the text lenght allowed is 200 characters.
 - it is sufficient for most URLs, emails, phone numbers, etc.

# Used Python Packages:
- wxPython For GUI operations.
- Pyqcode	For generating QR code easily.
- Pypng	For generating png images. (required by Pyqcode)

# Used Tools:
 - wxFormBuilder: A tool to build GUI forms visually based on wxPython library.

# How to run the project on Windows:

 - Make sure you have Python 3 installed;
 - Unzip the project to your desired location;
 - Navigate in Windows Explorer or cmd to the location;
 - Launch: python Main.pyw or python -3 Main.pyw
 - Don't worry about installing required packages,  
   the program designed to take care of that at the first run (Check py/InstallPkg.py if interested to know how)

# How to run the project on Linux:
 - to be documented;

# How to run the project on Mac:
 - to be documented;

# Features which can be added:

 - "save as..." button to be able to save the QR Code under different formats: Vector and Bitmap Image File Formats;

 - "share" button for sharing on social media;

 - "about" button for explaining what it is about and how to use it;

 - "mail" button to be able to send the QR Code in a new e-mail, with 2 options: as attachment or as picture inserted;

 - expand the default limit from 200 characters to standard:

http://en.wikipedia.org/wiki/QR_code
Numeric only Max. 7,089 characters (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) Alphanumeric Max. 4,296 characters (0–9, A–Z [upper-case only], space, $, %, *, +, -, ., /, :) Binary/byte Max. 2,953 characters (8-bit bytes) (23624 bits) Kanji/Kana Max. 1,817 characters

 - Ctrl+A is not available for text manipulation. Ctrl+C/Ctrl+V are available;

 - Ctrl+C is not available for copying the QR Code;

 - allow a history view for the last X texts used so far; If X <= n keep the texts in memory else write them to a file.
