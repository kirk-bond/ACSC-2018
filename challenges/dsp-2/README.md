## dsp-2

<xkcd.jpg>

To read the file into python:

```python
f = open('dsp_2.iq', 'rb')

# read the IQ data from the file as np.complex
rx_signal = scipy.fromfile(f, dtype=np.complex)

f.close()
```

## Flag

`acsc18{pwn_the_rfz}`

## Category

Miscellaneous (Digital Signal Processing)

## Hints

1. This is an OFDM burst
2. Autocorrelation is your friend
3. The FFT size is 128
4. There are 16 guard subcarriers, no DC subcarrier
5. The subcarriers are QPSK modulated

## Steps

See `solve.py`.

## Resources Required

* Just the file (dsp_2.iq)
