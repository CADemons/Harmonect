#!/usr/bin/env python
import sys, time
from mingus.midi import fluidsynth
from mingus.containers import Note, NoteContainer

if sys.platform == 'linux2':
    fluidsynth.init('GeneralUser GS v1.471.sf2', 'alsa')
else:
    fluidsynth.init('GeneralUser GS v1.471.sf2')

fluidsynth.set_instrument(1, int(sys.argv[1]), int(sys.argv[2]))

c = Note("C-4")
e = Note("E-4")
g = Note("G-4")

fluidsynth.play_Note(c)
time.sleep(2)

fluidsynth.play_Note(e)
time.sleep(2)

fluidsynth.play_Note(g)
time.sleep(2)

fluidsynth.stop_Note(c)
fluidsynth.stop_Note(e)
fluidsynth.stop_Note(g)
time.sleep(2)

nc = NoteContainer(["C-4", "E-4", "G-4"])
nc.velocity = 70
fluidsynth.play_NoteContainer(nc)
time.sleep(2)

fluidsynth.stop_NoteContainer(nc)
