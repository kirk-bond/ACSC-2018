import numpy as np
import matplotlib.pyplot as plt
import commpy.modulation
import scipy
import sys

def main():

    f = open('dsp_challenge2.iq', 'rb')

    # read the IQ data from the file as np.complex
    rx_signal = scipy.fromfile(f, dtype=np.complex)

    f.close()

    plt.figure()
    plt.plot(np.real(rx_signal), 'r')
    plt.plot(np.imag(rx_signal), 'b')
    plt.title("Plot 0:\nReceived Signal - Time Domain Plot\n (Very well defined burst visible, easy to find the start)")

    plt.figure()
    plt.plot(np.abs(np.fft.fftshift(np.fft.fft(rx_signal))))
    plt.title("Plot 1:\nReceived Signal - Frequency Domain Plot (Looks a lot like OFDM to me...)")

    # Get the start position from the Time Domain plot
    # approximate the length
    start = 1024
    length = 800

    # pull out the burst for processing
    received_burst = rx_signal[start:start+800]

    # compute the autocorrelation to find the OFDM symbol len
    autocorr = np.correlate(received_burst, received_burst, mode='full')

    plt.figure()
    plt.plot(np.abs(autocorr[len(autocorr)/2:]))
    plt.title("Plot 2:\nAutocorrelation, note the peak at 144")

    # get the symbol length from the autocorrelation plot
    symbol_len = 144

    # this is a logical fft size based on the symbol length
    fft_size = 128

    # this is the precise length of the burst
    burst_len = 144 * 5

    rx_symbols = []

    # Extract OFDM symbols from the received burst,
    # remove the cyclic prefixes
    for i in range(len(received_burst)/symbol_len):

        rx_symbol = np.zeros(symbol_len, dtype=np.complex)

        for k in range(symbol_len):
            rx_symbol[k] = received_burst[i*symbol_len + k]

        rx_symbols.append(np.fft.fftshift(np.fft.fft(rx_symbol[-fft_size:])))

    # plot the magnitude of the received OFDM symbols
    # this will show if there are pilots, DC subcarrier, or guard bands present

    plt.figure()
    for i in rx_symbols:
        plt.plot(np.abs(i))

    plt.title("Plot 3:\nOFDM Symbol magnitudes")

    # Plotting the magnitudes shows that there is no DC subcarrier,
    # no pilots, and 8 guard bands on each side.  Very simple to pull
    # the data out.

    num_guard = 16
    num_left_guard = 8

    num_data_subcarriers = fft_size - num_guard

    rx_data_array = np.zeros(len(rx_symbols) * num_data_subcarriers, dtype=np.complex)

    # Pull out the data subcarriers
    for i in range(len(rx_symbols)):
        for k in range(num_data_subcarriers):
            rx_data_array[i*num_data_subcarriers + k] = rx_symbols[i][k+num_left_guard]

    # Plot the constellation diagram to see what we've got
    plt.figure()
    plt.plot(np.real(rx_data_array), np.imag(rx_data_array), 'ro')
    plt.title("Plot 4:\nNice looking QPSK constellation plot")

    # time to demodulate the QPSK!!!

    # use commpy to demodulate, if you use something else
    # and your constellation mapping is different, you
    # will need to do a small amount of brute forcing
    qpsk_modem = commpy.QAMModem(4)

    # do hard decoding
    demodulated_data = qpsk_modem.demodulate(rx_data_array, 'hard')

    # time to deal with the bits
    bitstring = ''

    for i in demodulated_data:
        bitstring += str(i)

    plt.show()

    sys.stdout.write('\n')
    for i in range(0,len(bitstring),8):
        sys.stdout.write("%s" % chr(int(bitstring[i:i+7], 2)))

    sys.stdout.write('\n\n')

if __name__ == '__main__':
    main()
