#
# test_plot.py - Written by Jack Keegan
# Last updated 16-1-2014
#
# This short Python program receives data from the
# BioSemi ActiveTwo acquisition system via TCP/IP.
#
# Each packet received contains 16 3-byte samples
# for each of 8 channels. The 3 bytes in each sample
# arrive in reverse order (least significant byte first)
#
# Samples for all 8 channels are interleaved in the packet.
# For example, the first 24 bytes in the packet store
# the first 3-byte sample for all 8 channels. Only channel
# 1 is used here - all other channels are discarded.
#
# The total packet size is 8 x 16 x 3 = 384.
# (That's channels x samples x bytes-per-sample)
#
# 512 samples are accumulated from 32 packets.
# A DFT is calculated using numpy's fft function.
# the first DFT sample is set to 0 because the DC
# component will otherwise dominates the plot.
# The real part of the DFT (all 512 samples) is plotted.
# That process is repeated 50 times - the same
# matplotlib window is updated each time.
#

# Modified and simplified by Roger Anguera, 09/2016 for Neuroscape imotions integration
# Returns matrix of num_channels*num_packets
# roger.anguera@ucsf.edu
 
import socket


def get_biosemi_samples(ip, port, num_channels, packet_size, buffer_size):
	# Open socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip,port))
	     
	# Read the next packet from the network
	data = s.recv(buffer_size)
	samples = [[0 for x in range(packet_size)] for y in range(num_channels)]

	# Extract 16 samples from channel-1. Samples/chunk is shown on avtiview
	for m in range(packet_size):
		for x in range(num_channels):
		    offset = x * 3
		    # The 3 bytes of each sample arrive in reverse order
		    sample = (ord(data[offset+2]) << 16)
		    sample += (ord(data[offset+1]) << 8)
		    sample += ord(data[offset])
		    samples[m].append(sample)
	 
	# Close socket
	s.close()

	return samples
