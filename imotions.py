# Parses samples array into imotions format and sends via UDP
# Roger Anguera, 09/2016 - roger.anguera@ucsf.edu

import socket

def UDPToImotions(ip, port, samples):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    string_for_iMotions = ArrayToImotionsXML(samples)
    sock.sendto(bytes(ArrayToImotionsXML(samples),"utf-8"),(ip,port))

    # Example
    # for i in range(0,100):
    #     string_for_iMotions="E;1;EventSourceId;1;0.0;;;SampleId;" + str(i) + ";" + str(i/10) + "\r\n"
    #     sendudp(string_for_iMotions)
    #     time.sleep(.5)
    #     print("Sending Data to Port " + str(UDP_PORT))

    def ArrayToImotionsXML(samples):
        s = "E;1;Biosemi;1;0.0;;;EEG;"
        for x in range(0,len(samples-1)):
            s += str(samples[x])+";"
        s += str(samples[len(samples-1)])
        s += "\r\n"
        return s
