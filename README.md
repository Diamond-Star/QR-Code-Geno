# QR-Code-Geno
A simple GUI project based on Python 3 with the scope to generate a QR Code.

How to run the project on Windows:
 - make sure you have Python 3 installed;
 - unzip the project to your desired location;
 - navigate in cmd to the location;
 - make sure your system satisfies all the requirements: pip install -r requirements.txt
 - launch: python Main.pyw or python -3 Main.pyw
 
 How to run the project on Linux:
 - to be documented;
  
 How to run the project on Mac:
 - to be documented;
 
 Features which can be added:
 - "save as..." button to be able to save the QR Code under different formats: Vector and Bitmap Image File Formats;
 - allow the QR Code resolution to be adjustable. Ex: 600 x 600, 800 x 800, 1024 x 1024, etc;
 - allow the background color for the QR code to be adjustable. Ex: On click pick a random gray/(other random color);
 - allow the foreground color for the QR code to be adjustable. Ex: On click pick a random color but not the same as background;
 - add single color, color gradient and/or custom eye color options; 
 - add body Shape, eye frame shape, eye ball shape options or templates;
 - add "insert custom logo" option; make available by default some most used logos: GitHub, FB, Twitter, YouTube, Insta, etc. 
 - "share" button for sharing on social media;
 - "about" button for explaining what it is about and how to use it;
 - "mail" button to be able to send the QR Code in a new e-mail, with 2 options: as attachment or as picture inserted; 
 - expand the default limit from 200 characters to standard:
   
   * http://en.wikipedia.org/wiki/QR_code

    Numeric only    Max. 7,089 characters (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    Alphanumeric    Max. 4,296 characters (0–9, A–Z [upper-case only], space, $, %, *, +, -, ., /, :)
    Binary/byte     Max. 2,953 characters (8-bit bytes) (23624 bits)
    Kanji/Kana      Max. 1,817 characters

 - Ctrl+A is not available for text manipulation. Ctrl+C/Ctrl+V are available;
 - Ctrl+C is not available for copying the QR Code;
 - allow a history view for the last X texts used so far; If X <= n keep the texts in memory else write them to a file.
