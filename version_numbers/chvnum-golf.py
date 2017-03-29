#!/usr/bin/env python3
import sys
def showhelp():
	print("checkversionnumber.py ((-h|--help)|{First version} {Second version})")
	sys.exit(0)
if(len(sys.argv)>1):
	if (sys.argv[1] == '--help' or sys.argv[1]=='-h'): showhelp();
else: showhelp();
if len(sys.argv) == 3:
	if(len(sys.argv[1].split('.')) != len(sys.argv[2].split('.'))):
		sys.stderr.write("\033[1;31mThese version numbering schemes don't match\033[m\nPlease try a different set, where there is an equal number of sub-versions.\n");
		exit(1);
	for i in range(0,len(sys.argv[1].split('.'))):
		if(int(sys.argv[1].split('.')[i]) < int(sys.argv[2].split('.')[i])): print("Second is newer.");
		elif (int(sys.argv[1].split('.')[i]) > int(sys.argv[2].split('.')[i])): print("First is newer.");
		if(int(sys.argv[1].split('.')[i])!=int(sys.argv[2].split('.')[i])): sys.exit(0);
	print("These are the same.")
else:
	sys.stderr.write("\033[1;31mInvalid arguments.\033[m\nExiting now.\n")
