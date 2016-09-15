"""

Python BioSemi ActiveTwo: main class
Copyright 2015, Ilya Kuzovkin
Licensed under MIT

https://github.com/kuz/pyactivetwo

Builds on example code by Jack Keegan
https://batchloaf.wordpress.com/2014/01/17/real-time-analysis-of-data-from-biosemi-activetwo-via-tcpip-using-python/

"""

# Modified and simplified and merged with https://github.com/kuz/pyactivetwo/blob/master/pyactivetwo/pyactivetwo.py
# by Roger Anguera, 09/2016 for Neuroscape imotions integration
# Returns matrix of num_samples*num_channels
# roger.anguera@ucsf.edu
 
import socket
import numpy as np


class Biosemi():

	ip = None
	port = None
	nchannels = None
	buffer_size = None

	def __init__(self, _ip, _port, _nchannels, _tcpsamples):

		# store parameters
		self.ip = _ip
		self.port = _port
		self.nchannels = _nchannels
		self.tcpsamples = _tcpsamples
		self.buffer_size = self.nchannels * self.tcpsamples * 3

		# open connection
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.ip, self.port))

	def read(self):

		# Create a 16-sample signal_buffer
		signal_buffer = np.zeros((self.nchannels, self.tcpsamples))

		# Read the next packet from the network
		# sometimes there is an error and packet is smaller than needed, read until get a good one
		data = []
		while len(data) != self.buffer_size:
			data = self.s.recv(self.buffer_size)

		# Extract 16 samples from the packet (ActiView sends them in 16-sample chunks)
		for m in range(self.tcpsamples):
			# extract samples for each channel
			for ch in range(self.nchannels):
				offset = m * 3 * self.nchannels + (ch * 3)

				# The 3 bytes of each sample arrive in reverse order
				sample = (ord(data[offset+2]) << 16)
				sample += (ord(data[offset+1]) << 8)
				sample += ord(data[offset])

				# Store sample to signal buffer
				signal_buffer[ch, m] = sample

		# transpose matrix so that rows are samples
		signal_buffer = np.transpose(signal_buffer)

		return signal_buffer

	def disconnect(self):
		self.s.close()
