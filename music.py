"""
music.py - handles music

Primary author: Colin Rioux (@colinrioux)
Supporting authors: Linc Berkeley (@lincb)

"""
import math, time, yaml, os, types
import numpy as np
import mingus.core.scales as scales
from mingus.midi import fluidsynth
from mingus.containers import Note
from mingus.containers import NoteContainer

fluidsynth.init("GeneralUser GS v1.471.sf2")

class StepPlayer:

    """
    Stores a scale and intrument data. Able to quickly play any given step array.
    :type steps: int
    :param steps: The number of steps, corresponding to the number of possible notes.

    :type sc: String
    :param sc: Scale name. Optional.

    :example:
    ex = State([True, True, False])

    """
    def __init__(self, numSteps, scaleName="Diatonic", start_key='C'):
        self.numSteps = numSteps
        self.scaleName = scaleName
        self.start_key = start_key
        self.soundArr = self.__getSoundArr()

    def __str__(self):
        return 'Map: {0}\nScale: {1}\nStart Key: {2}'.format(self.soundArr, self.scaleName, self.start_key)

    """
    Creates an array of NoteContainers corresponding to the selected scale.
    """
    def __getSoundArr(self, startOc=4):
        tmp = []
        scl = self.__scaleArray()
        oc = startOc - 1
        firstNote = scl[0]
        for note in scl:
            if note == firstNote:
                oc += 1
            tmp.append(NoteContainer(Note(note, oc)))
        return tmp

    """
    Builds scale.

    :private:

    """
    def __buildScale(self):
        octa = int(math.ceil((self.numSteps / 7.0)))
        return {
            "diatonic": scales.Diatonic(self.start_key, (3, 7), octa),
            "ionian": scales.Ionian(self.start_key, octa),
            "dorian": scales.Dorian(self.start_key, octa),
            "phrygian": scales.Phrygian(self.start_key, octa),
            "lydian": scales.Lydian(self.start_key, octa),
            "mixolydian": scales.Mixolydian(self.start_key, octa),
            "aeolian": scales.Aeolian(self.start_key, octa),
            "locrian": scales.Locrian(self.start_key, octa),
            "major": scales.Major(self.start_key, octa),
            "harmonicmajor": scales.HarmonicMajor(self.start_key, octa),
            "naturalminor": scales.NaturalMinor(self.start_key, octa),
            "harmonicminor": scales.HarmonicMinor(self.start_key, octa),
            "melodicminor": scales.MelodicMinor(self.start_key, octa),
            "bachian": scales.Bachian(self.start_key, octa),
            "minorneapolitan": scales.MinorNeapolitan(self.start_key, octa),
            "chromatic": scales.Chromatic(self.start_key, int(math.ceil((self.numSteps / 12.0)))),
            "wholetone": scales.WholeTone(self.start_key, int(math.ceil((self.numSteps / 6.0)))),
            "octatonic": scales.Octatonic(self.start_key, int(math.ceil((self.numSteps / 8.0))))
        }.get(self.scaleName.lower(), "custom")

    """
    If the scale is custom, it reads the yaml file (if it exists) and returns the yaml.

    """
    def __buildCustomScale(self, name):
        ls = os.listdir('./scales')
        filename = ''
        for item in ls:
            if item == (name.lower() + '.yml'):
                filename = item
        if filename is '': raise ValueError('Custom scale doesn\'t exist!')
        with open('./scales/' + filename, 'r') as f:
            doc = yaml.load(f)
        return doc

    """
    Builds ascending array for a custom scale.

    """
    def __handleCustom(self, notes, r):
        return notes * r + [notes[0]]


    """
    Converts scale object to an array.

    :type scl: Scale Object
    :param scl: Ideally from func buildScale().

    :type mode: String
    :param mode: Scale mode. Valid values include: `asc` & `desc`. Optional.

    :private:

    """
    def __scaleArray(self, mode="asc"):
        scl = self.__buildScale()
        if type(scl) == types.StringType and scl == "custom":
            d = self.__buildCustomScale(self.scaleName.split(' ')[1])
            return {
                "asc": self.__handleCustom(d['ascending'].split(' '), d['range']),
                "desc": self.__handleCustom(d['ascending'].split(' '), d['range']).reverse() 
            }.get(mode, "Invalid mode!")
        else:
            return {
                "asc": scl.ascending(),
                "desc": scl.descending()
            }.get(mode, "Invalid mode!")

    """
    Plays music corresponding to the given array of steps.
    """
    def processSteps(self, steps, oldSteps=None):
        if oldSteps is not None:
            steps = getNewSteps(steps, oldSteps)
        for step, sound in zip(steps, self.soundArr):
            if step:
                fluidsynth.play_NoteContainer(sound)

"""
Finds the steps that are new in the current step array.

:type currentSteps: list
:param currentSteps: The current step array, such as one produced by step_detect.getStepArr

:type oldSteps: list
:param oldSteps: The old step array to subract, such as one produced by step_detect.getStepArr
"""
def getNewSteps(currentSteps, oldSteps):
    return np.logical_and(currentSteps, np.logical_not(oldSteps))

if __name__ == '__main__':
    # player = StepPlayer(10, "Diatonic", "A")
    # player.processSteps([True, True, False, False, False, False, True, False, True, True])
    # print player
    player = StepPlayer(10, "Custom Major")
    player.processSteps([True, True, False])
    print player
    time.sleep(4)
    # fluidsynth.play_NoteContainer(NoteContainer(p.ascending())