# Sends live biosemi eeg data into imotions
# Roger Anguera, 09/2016 - roger.anguera@ucsf.edu

biosemi_ip = "127.0.0.1"
biosemi_port = 8888
biosemi_num_channels = 8
biosemi_buffer_size = 384 # see actiview. depends on num channels
biosemi_packet_size = 16 # see actiview. depdends on sampling rate

imotions_ip = "127.0.0.1"
imotions_port = 8889

import imotions
import biosemi

samples = get_biosemi_samples(biosemi_ip,biosemi_port,biosemi_num_channels,
	biosemi_packet_size,biosemi_buffer_size)

for x in xrange(len(samples)):
	UDPToImotions(imotions_ip, imotions_port, samples[x])