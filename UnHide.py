#!/usr/bin/python2
#!/usr/env python2

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
	Do not Paste and Copy it.
	Changing the Variabel and the Author Name didn't make You be a Programmer '''
# Note: ASCII Art is copyrighted to Artist Unknown with Title "Crying Eye"
#       visit: http://ascii.co.uk/art/eye

import platform,os,argparse,socket,httplib
if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')
def jeda():
	raw_input("Press [ENTER] ")

parser = argparse.ArgumentParser()
parser.add_argument("--target",dest='target',help='Specify the Target HOST/IP',type=str)
parser.add_argument("--pagelist",dest='pagelist',help='Specify Page List to use',type=str,default='./page/mxact666_pagelist.txt')
options = parser.parse_args()

if options.target == '' or options.target == 'None' or options.target == None:
	print ""
	print "[!] Error: Target unidentificated! Please check again"
	print "           Your command! learn on 'EXAMPLE.txt'"
	print "           or You can try run 'UnHide.py --help' command"
	print ""
	jeda()
	exit()

try:
	print ""
	ip_address = socket.gethostbyname(options.target)
except:
	print "[!] Error: Can't find IP Address from {0}".format(options.target)
	print "           check Your connection or check the Host Address!"
	print ""
	jeda()
	exit()
try:
	isi_wlist = open(options.pagelist,'r').readlines()
except:
	print "[-] Error: Can't open or read Wordlist! check Location"
	print "           or try again. Wordlist File's is may too big"
	print "           or corrupted"
	print ""
	jeda()
	exit()
jumlah_kata = str(len(isi_wlist))

print """
             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..         UnHide.py ---> Login Page
    ,,''                    '';;;;,;''                       Finder
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.   Coded by M-XacT-666 (copyright)
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;   Target     : {0}
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.  IP Address : {1}
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;  Page List  : {2}
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'  Total Page : {3}
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
""".format(options.target,ip_address,options.pagelist,jumlah_kata)

hitung = 0
print ""
confirm = raw_input("Confirmation (Y/n) > ")
if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "NO" or confirm == "No":
	print ""
	print "[-] Cracking Canceled with Confirmation..."
	print ""
	exit()
else:
	pass
print ""

target = str(options.target)

for halaman in isi_wlist:
	page = halaman.strip()
	url = target+page
	hitung+=1
	try:
		konak = httplib.HTTPConnection(target)
		konak.connect()
		konak.request("GET",page)
		balasan = konak.getresponse()
		nomor_balas = balasan.status
		if nomor_balas == 200:
			print ""
			print "[ 200 ]===({0}/{1})===> {2}".format(hitung,jumlah_kata,url)
			break
		else:
			print "[ {0} ]===({1}/{2})===> {3}".format(nomor_balas,hitung,jumlah_kata,url)
	except KeyboardInterrupt:
		print ""
		print "[-] Cracking Canceled with Keyboard Interrupt by User..."
		print ""
		jeda()
		exit()
	except:
		print ""
		print "[!] Error: Unknown Error has been occured! Sorry :("
		print "           This problem may caused by Your Internet Connection!"
		print ""
		jeda()
		exit()