#Alright, this is the next logical step. we are going to create a script
# that changes tempo, chords, and time signature, every "measure"
# let's see what we can do i guess..


#imports the needed modules the midifile from midiutil
from midiutil import MIDIFile
import random as r

#establishes the varibles and "libraries" of notes and time
arpArray = ([60,64,67,72],[61,65,68,73],
 [62,66,69,74],[63,67,70,75],
 [64,68,71,76],[65,69,72,77],
 [66,70,73,78],[67,71,74,79],
 [68,72,75,80],[57,61,64,69],
 [58,62,65,70],[59,63,66,71],
 
 [60,63,67,72],[61,64,68,73],
 [62,65,69,74],[63,66,70,75],
 [64,67,71,76],[65,68,72,77],
 [66,69,73,78],[67,70,74,79],
 [68,71,75,80],[57,60,64,69],
 [58,61,65,70],[59,62,66,71])


track   = 0
channel = 0
time    = 0
duration= 1
bNote   = 0
bDur    = 0
bTime   = 0
tempo   = 120
volume  = 100

#Choice of Time signatures.. there is probably a better way to do this
timeSigs = ([0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0])

#Creates the MIDIFile object and initializes the track and assigns tracknames
MyMidi = MIDIFile(4)
MyMidi.addTempo(track, time, tempo)
MyMidi.addTrackName(0, 0, "arpArray")
MyMidi.addTrackName(1, 0, "Bass")

#Song loop
while time < 125:
    key = r.choice(arpArray)
    meter = r.choice(timeSigs)
    bDur = len(meter) * 0.25
    bNote = key[0] - 12
    MyMidi.addNote(1,1, bNote, bTime, bDur, volume)
    bTime += len(meter) * 0.25
    for notes in meter:
        pitch = r.choice(key)
        MyMidi.addNote(0,0,pitch, time, 0.25, volume)
        time += 0.25
    tempo = r.randrange(35, 200)
    MyMidi.addTempo(track, time, tempo)
    

with open("test5.mid", "wb") as output_file:
    MyMidi.writeFile(output_file)