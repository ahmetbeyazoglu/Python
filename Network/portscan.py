#!/usr/bin/python
from socket import *
import optparse 
from threading import *

def connScan(Host, Port):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((Host,Port))
		print '[+] %d/tcp Open' % Port
	except:
		print '[-] %d/tcp Closed' % Port
	finally:
		sock.close()
		
def portScan(Host, Ports):
	try:
		IP = gethostbyname(Host)
	except:
		print 'Unknown Host %s' %Host 
	try:
		tgtName = gethostbyaddr(IP)
		print '[+] Scan results for: ' + tgtName[0]
	except:
		print '[+] Scan results for: ' + IP
	setdefaulttimeout(1)
	for Port in Ports:
		t = Thread(target=connScan, args=(Host, int(Port)))
		t.start()

def main():
	parser = optparse.OptionParser('Usage of program:  ' + '-u <target host> -p <target port> \n example: ./portscan -u 10.10.10.10 -p 22,80,21')
	parser.add_option('-u', dest='Host', help='specify target host')
	parser.add_option('-p', dest='Port', help='specify target ports seperated by comma')
        (options, args) = parser.parse_args()
	Host = options.Host
	Ports = str(options.Port).split(',')
	if (Host == None) | (Ports[0] == None):
		print parser.Usage
		exit(0)
	portScan(Host,Ports)

if __name__ == "__main__":
	main()