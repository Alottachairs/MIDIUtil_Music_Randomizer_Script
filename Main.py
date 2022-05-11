
#imports the needed modules the midifile from midiutil
from midiutil import MIDIFile
import random as r

#establishes the varibles and "libraries" of notes and time
arpArray = ([60,64,67,71],[61,65,68,72], #All 12 Major 7th chords
 [62,66,69,73],[63,67,70,74],
 [64,68,71,75],[65,69,72,76],
 [66,70,73,77],[67,71,74,78],
 [68,72,75,79],[57,61,64,68],
 [58,62,65,69],[59,63,66,70],
 
 [60,63,67,70],[61,64,68,71], #All 12 Minor 7th chords
 [62,65,69,72],[63,66,70,73],
 [64,67,71,74],[65,68,72,75],
 [66,69,73,76],[67,70,74,77],
 [68,71,75,78],[57,60,64,67],
 [58,61,65,68],[59,62,66,69])

track   = 0
channel = 0
time    = 0
duration= 1
bNote   = 0
bDur    = 0
bTime   = 0
dNote   = [48,53,53,53,49,53,53,53,57]
dCount  = 1
dTime   = 0
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
MyMidi.addTrackName(2, 0, "808 kit")

#Song loop
while time < 125: # length of the song Each loop = 1 measure
    key = r.choice(arpArray) # chooses the key of the measure
    meter = r.choice(timeSigs) # chooses the meter of the measure
    bDur = len(meter) * 0.25 
    bNote = key[0] - 12
    MyMidi.addNote(1,1, bNote, bTime, bDur, volume) #writes bass note
    bTime += len(meter) * 0.25
    for drums in dNote:
        MyMidi.addNote(2, 2, drums, dTime, 0.25, volume)
        dCount += 1
        dTime += 0.25
        if dCount > len(meter):
            break      
    for notes in meter: # Creates arpeggios in key
        pitch = r.choice(key)
        MyMidi.addNote(0,0,pitch, time, 0.25, volume)
        time += 0.25
    tempo = r.randrange(28, 180) # choose then write new tempo for next measure
    MyMidi.addTempo(track, time, tempo)
    dCount = 1
    
# Writes the midi file
with open("yourRapture.mid", "wb") as output_file:
    MyMidi.writeFile(output_file)