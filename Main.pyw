"""
Main.py
This is the main file in the program that runs it.
"""
import os

# Check if "py/InstallPkg.py" file exists, so we know this the first run of the program.
# And we have to install Python packages.
if os.path.exists("py/InstallPkg.py"):
	# Run the file by OS system shell command.
	os.system("python py/InstallPkg.py")
	# Rename it so this process will be skipped at the next run.
	os.rename("py/InstallPkg.py", "py/InstallPkg.py.del")
	
# Run the script to actually start the program and show the window.
# os.popen() used to execute OS commands like os.system() but the console window is not shown.
os.popen("pythonw py")

