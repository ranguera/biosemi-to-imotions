# Parses sample array into imotions format and sends via UDP
# Roger Anguera, 09/2016 - roger.anguera@ucsf.edu

import socket

class Imotions():

    ip = ""
    port = 0
    sock = None

    def __init__(self, _ip, _port):
        ip = _ip
        port = _port
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       

    def UDPToImotions(sample):
        string_for_iMotions = ArrayToImotionsXML(sample)
        sock.sendto(bytes(ArrayToImotionsXML(sample),"utf-8"),(ip,port))


    def ArrayToXML(sample):
        s = "E;1;Biosemi;1;0.0;;;EEG;"
        for x in range(0,len(sample-1)):
            s += str(samples[x])+";"

        s += str(samples[len(sample-1)])
        s += "\r\n"
        return s

    def Disconnect():
        sock.close()