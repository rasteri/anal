from scipy.io import wavfile # scipy library to read wav files
import numpy as np

def column(matrix, i):
    return [row[i] for row in matrix]

freqs1 = [
            [20.0, 12.5, 0.0],
            [25.0, 24.5, 0.0],
            [31.5, 37, 0.0],
            [40.0, 48.5, 0.0],
            [50.0, 60.5, 0.0],
            [63.0, 72, 0.0],
            [80.0, 83.5, 0.0],
            [100.0, 95, 0.0], 
            [125.0, 107.5, 0.0], 
            [160.0, 119.5, 0.0], 
            [200.0, 131.5, 0.0], 
            [250.0, 144, 0.0], 
            [315.0, 156, 0.0], 
            [400.0, 168, 0.0], 
            [500.0, 180, 0.0], 
            [630.0, 192.5, 0.0], 
            [800.0, 204, 0.0], 
            #[1000.0, 216, 0.0],
          ]

#1000 is at 230.5

freqs2 = [
        [1250.0, 243.5, 0.0],
        [1600.0, 256, 0.0],
        [2000.0, 268, 0.0],
        [2500.0, 280 , 0.0],
        [3150.0, 293, 0.0],
        [4000.0, 305.2, 0.0],
        [5000.0, 317, 0.0],
        [6300.0, 330, 0.0],
        [8000.0, 342, 0.0],
        [10000.0, 354, 0.0],
        [12500.0, 366.5, 0.0],
        [16000.0, 379, 0.0],
        [20000.0, 392, 0.0],
        #[1000.0,  403.5 , 0.0],
        ]

# return amplitude of a section of audio where the start is at samp
def analband(samp, Audiodata, fs):
    total = 0.0
    
    #chop a second off start and end
    startsamp = fs * 1
    endsamp = fs * 9

    for bum in Audiodata[samp + startsamp:samp + endsamp]:
        total += ((float(bum[0]) + float(bum[1])) / 2.0) ** 2

    total /= (endsamp - startsamp)
    return np.sqrt(total)


def analfile(AudioName):

    freqs = []

    fs, Audiodata = wavfile.read(AudioName)

    ## reference 1000hz tone for first batch of freqs is at track start
    ref1 = analband(0, Audiodata, fs)

    print ("ref1 db", 20*np.log10(ref1 / 2.0**31))

    # now do other bands
    for freq in freqs1:
        currsamp = int(freq[1] * fs)
        res = [freq[0], 20*np.log10(analband(currsamp, Audiodata, fs) / ref1)]
        freqs.append(res)
        print(res[0], res[1], ",")

    # ref tone for second batch of freqs is at 230.5sec   
    ref2 = analband(int(230.5 * fs), Audiodata, fs)

    # now do other bands
    for freq in freqs2:
        currsamp = int(freq[1] * fs)
        res = [freq[0], 20*np.log10(analband(currsamp, Audiodata, fs) / ref2)]
        freqs.append(res)
        print(res[0], res[1], ",")
    
    return fs, freqs


# Plot the audio signal in time
import matplotlib.pyplot as plt

fs, freqs = analfile("PDX3000 S-ARM M44-7 DJM-750.wav")

plt.figure()
plt.xscale('log')
plt.plot(column(freqs, 0), column(freqs, 1))
plt.xlabel('Frequency (Hz)'); plt.ylabel('RMS compared to ref (dB)');
plt.show()
#analfile("big.wav")