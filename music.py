# music.py - 
import mingus.core.notes as notes
#import mingus.core.scales as scales
from mingus.midi import fluidsynth
from mingus.containers import Note

def processSteps(steps):
	"""
	Play music when a person is standing on a specific step.

	:type steps: Boolean Array
	:param steps: an array which is mapped to the current configuration of steps. 

	@example
	processSteps([True,False,False,False])
	==> maps steps: step 1 = steps[0], step 2 = steps[1], etc etc.
	==> for all true steps, play a specific note

	"""

	# while loop so it continues to play via current state definied by an initialization of a state object.
	#fluidsynth.init("GeneralUser GS v1.471.sf2") 
	current_state = State(steps)
	print(current_state.map)

	#fluidsynth.play_Note(Note("C"))

	

print("No Errors!")

class State:

	def __init__(self, steps):
		self.steps = steps
		self.map = self.__drawMap()

	def __drawMap(self):
		tmp = []
		dia = ["C", "D", "E", "F", "G", "A", "B"]
		for x in range(0, len(self.steps)):
			if (x >= 7):
				tmp.append(dia[x-7])
			else:
				tmp.append(dia[x])
		return tmp



processSteps([True,False,False,False,False,False,False])
#print(notes.int_to_note(9))