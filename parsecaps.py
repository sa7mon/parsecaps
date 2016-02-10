###############################################
#
# parsecaps.py - Parses wpa.cap from besside-ng and 
# 		 creates individual .caps for each network
#
# Currently must be run from same directory wpa.cap is stored in. 
# Usage: python ./parsecaps.py
#
# Created on: 2/7/16
# Created by: Dan Salmon
#	@bltjack | github.com/sa7mon | https://danthesalmon.com
# 
##############################################

#!/usr/bin/python
import subprocess, sys, getopt

def showHelp():
    print 'Usage: parseCaps.py [options] capfile.cap\n'
    print 'Options:'
    print '  -o, --outfolder        Folder to place all the cap files'
    print '  -n, --networks         Output names of networks with handshakes'

def main(argv): 
    inputCapFile = ''
    outFolder = ''
    try:
        opts, args = getopt.getopt(argv,"hon",["outfolder","networks"])
    except getopt.GetoptError:
        showHelp()
        sys.exit(2)
    for opt, arg in opts:
        print opt, arg
        if opt == "-h":
            showHelp()
        elif opt in ("-o", "--outfolder"):
            print '-o argument set.'
        elif opt in ("-n", "--networks"):
            print '-n argument set.'
        else:
            print "Unrecognized argument: " + opt
            sys.exit()
	# p = subprocess.Popen(['pyrit', '-r', 'wpa.cap', 'analyze'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	# grepExec = subprocess.Popen(['grep', 'AccessPoint'], stdin=p.stdout, stdout=subprocess.PIPE)
	# out, err = grepExec.communicate()
	# handshakeCount = 0
	# #print "Found handshakes:\n"
	# #print out
	# networks = {}

	# for line in out.split("\n"):
	# 	# Do something with each line.
	# 	if (len(line) > 0):
	# 		handshakeCount += 1
	# 		# Get MAC address of AP
	# 		APIndex = line.index("AccessPoint ")+11
	# 		mac = line[APIndex+1:APIndex+18]
	# 		# Get SSID of network 
	# 		SSID = line[line.index("('")+2:len(line)-3]
	# 		print mac + " - " + SSID
	# 		# Add the SSID and MAC address to the dictionary
	# 		networks[SSID] = mac
	# 		capfile = SSID + ".cap"
	# 		# Run Pyrit and create a cap for the network
	# 		pyritExec = subprocess.Popen(['pyrit', '-r', 'wpa.cap', '-o', capfile, '-e', SSID, 'strip'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	# 		out, err = pyritExec.communicate()
	# 		if err != "":
	# 			print pyritExecErr
		
	# print "Found handshakes: " + str(handshakeCount)

if __name__ == "__main__":
   main(sys.argv[1:])