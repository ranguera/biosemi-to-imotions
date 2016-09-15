# Parses sample array into imotions format and sends via UDP
# Roger Anguera, 09/2016 - roger.anguera@ucsf.edu

import socket

class Imotions():

	ip = ""
	port = 0
	sock = None

	def __init__(self, _ip, _port):
		self.ip = _ip
		self.port = _port
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		
	def ArrayToXML(self, sample):
		s = "E;1;Biosemi;1;0.0;;;EEG;"
		for x in range(0,len(sample)-1):
			s += str(sample[x])+";"

		s += str(sample[len(sample)-1])
		s += "\r\n"

		return s

		def Disconnect(self):
			sock.close()

	def UDPToImotions(self, sample):
		string_for_iMotions = self.ArrayToXML(sample)
		self.sock.sendto(string_for_iMotions.encode("utf-8"),(self.ip,self.port))
		print string_for_iMotions


	