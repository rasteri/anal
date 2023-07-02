# Anal

Python script to measure the frequency response of phonograph systems

You will need : 

1. Copy of Tacet's Vinyl: Check (https://www.tacet.de/main/seite1.php?language=en&filename=production.php&bestnr=02101)
2. Turntable with Cart/Stylus
3. Phono preamp
4. Sound card
5. Python


## Installation Instructions

1. Put anal.py in a folder
2. run "python -m pip install -r requirements.txt"


## Running Instructions

1. Record the frequency response section of Vinyl: Check (Part 9 - the second track on Side B) using the software of your choice
2. Trim the start of the recording so it begins on the very first 1000hz tone
3. Save it as a .wav file in the same folder as anal.py
4. Repeat parts 1-3 for each stylus/cartridge/preamp you want to test
5. Run anal.py ("python anal.py")
6. Look at the pretty graphs


## Examples

### Comparing various different combinations of Shure, Jico and Tonar cartridges and stylii:
This shows that the Jico carts and DJ Imp Nude stylii significantly attenuate the top end compared to the regular Shure M44-7 and Tonar stylus (although it should be noted that Jico are thought to be the manufacturers of the Tonar stylus).
![cheeart](examplegraphs/Figure_1.png?raw=true "cheeart")


### Examining the effect that high-capacitance cables have:
The increased capacitance attenuates higher frequencies.
![cheeart](examplegraphs/Figure_2.png?raw=true "cheeart")
