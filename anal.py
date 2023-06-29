from scipy.io import wavfile # scipy library to read wav files
import numpy as np

def analfile(AudioName):
    fs, Audiodata = wavfile.read(AudioName)

    avg_array = []
    for tu in Audiodata:
        avg_array.append((tu[0] / 2) + (tu[1] / 2) )

    Audiodata = avg_array



# spectrum
    from scipy.fftpack import fft # fourier transform
    n = 400000 #len(Audiodata) 
    AudioFreq = fft(Audiodata)
    AudioFreq = AudioFreq[0:int(np.ceil((n+1)/2.0))] #Half of the spectrum
    MagFreq = np.abs(AudioFreq) # Magnitude
    MagFreq = MagFreq / float(n)
# power spectrum
    MagFreq = MagFreq**2
    if n % 2 > 0: # ffte odd 
        MagFreq[1:len(MagFreq)] = MagFreq[1:len(MagFreq)] * 2
    else:# fft even
        MagFreq[1:len(MagFreq) -1] = MagFreq[1:len(MagFreq) - 1] * 2 

    from scipy.ndimage import gaussian_filter
    MagFreq = gaussian_filter(MagFreq, 2500)
    return fs,n,MagFreq

# Plot the audio signal in time
import matplotlib.pyplot as plt

fs, n, MagFreq = analfile("idealpink.wav")
fs2, n2, MagFreq2 = analfile("pinkgroovetool.wav")
fs2, n2, MagFreq3 = analfile("pinkaudiotechnica.wav")

av1 = np.mean(np.absolute(MagFreq))
av2 = np.mean(np.absolute(MagFreq2))
av3 = np.mean(np.absolute(MagFreq3))

MagFreq2 = np.multiply(MagFreq2, av1/av2)
MagFreq3 = np.multiply(MagFreq3, av1/av3)

plt.figure()
plt.xscale('log')
freqAxis = np.arange(0,int(np.ceil((n+1)/2.0)), 1.0) * (fs / n);

Diff1 = np.subtract(10*np.log10(MagFreq), 10*np.log10(MagFreq))
Diff2 = np.subtract(10*np.log10(MagFreq2), 10*np.log10(MagFreq))
Diff3 = np.subtract(10*np.log10(MagFreq3), 10*np.log10(MagFreq))

plt.plot(freqAxis/1000.0, Diff1, label="Ideal") #Power spectrum
plt.plot(freqAxis/1000.0, Diff2, label="Numark Groovetool") #Power spectrum
plt.plot(freqAxis/1000.0, Diff3, label="Audio Technica cheap shite") #Power spectrum

leg = plt.legend(loc='lower center')

plt.xlabel('Frequency (kHz)'); plt.ylabel('Power spectrum (dB)');

plt.figure()
plt.xscale('log')
freqAxis = np.arange(0,int(np.ceil((n+1)/2.0)), 1.0) * (fs / n);

plt.plot(freqAxis/1000.0, 10*np.log10(MagFreq), label="Ideal") #Power spectrum
plt.plot(freqAxis/1000.0, 10*np.log10(MagFreq2), label="Numark Groovetool") #Power spectrum
plt.plot(freqAxis/1000.0, 10*np.log10(MagFreq3), label="Audio Technica cheap shite") #Power spectrum

leg = plt.legend(loc='lower center')

plt.xlabel('Frequency (kHz)'); plt.ylabel('Power spectrum (dB)');


plt.show()