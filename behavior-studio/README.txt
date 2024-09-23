# Readme Setup Instructions for SWGEmu

## Behavior Studio Wiki: https://github.com/cas4ey/behavior-studio/wiki
## Setup Written using: https://github.com/cas4ey/behavior-studio/wiki/1.-Install

###1. Install Python27 32bit from here: https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi
	During Installation make sure pip is installed as well and Python27 select Add python.exe to Path. (bottom of options).
	RESTART YOUR COMPUTER.

###2. Install pip for Python 2.7
	Open PowerShell
	cd to C:/Python27
	Input: curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
	Input: python get-pip.py
	Make sure pip is installed with Input: python -m pip help

###3. From the same PowerShell terminal
	Input: pip install PySide==1.2.2
	Input: pip install lxml==3.4.4
	Input: pip install -U sortedcontainers

###4. cd to the directory in which behavior_studio is checked out to.

###5. Input: ./run_behavior_studio.bat
	Select File, Open Project.
	Navigate to data and then either SWGEmu or SWGEmuSpace directory for ground or space AI.
	Then select the .btprof file within the selected directory.

###6. When changing any portion of the tree, upon selecting the disk to save, the application will output an updated Lua file.
	Ensure to not push any Lua changes to Core3 without pushing the modified files from the selected directory to the Tools repository.





# behavior-studio Readme

## This is not needed if the above instructions were followed.

BehaviorStudio is a cross-platform behavior trees editor that allows you
to create, modify, view and save behavior trees in xml format.

Please, see Wiki page for more information!
https://github.com/cas4ey/behavior-studio/wiki


Windows:
1. Install Python 2.7 latest release
2. Navigate to Windows Environment Variables
3. Highlight Path and select Edit
4. Add C:\Python27 and C:\Python27\Scripts
5. Run "pip install -r requirements.txt" from behavior-studio
6. Run py compileall in behavior-studio/source
7. Run pip install regex
NOTE: Requires MS Visual C++ 9.0 for python2.7 found: https://web.archive.org/web/20190720195601/http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
8. Open "run_behavior_studio" batch file
