# Scales
We thought it'd be cool to implement custom scale defining in the event you don't want to use mingus' built in scales. 

## Format
For your custom scale, you must first create and save a new yaml file to this folder (`scales/`). For the built in yaml reader in `music.py` to work the way it was designed, the scale which you pass into the instantiator for a `StepPlayer()` must be spelt the same as the title of your yaml file. It must also be proceeded by the word `Custom` and then a space ` `. 

Take `major.yml` as an example. The custom scale name is `major`. The `major` scale is also a pre-defined mingus scale. 
```python
# If we wanted to use the predefined mingus scale, we would:
player = StepPlayer(numsteps, "Major", key_of_scale)

# If we wanted to instead use our custom defined major scale, we would:
player = StepPlayer(numsteps, "Custom Major", key_of_scale)
```
**Note: case is ignored when typing scale names. Therefore, `"cusToM MaJor"` would work as expected. Proper spelling and the space between custom and your scale name matters.**

Let's say that your scale name is two words. I.e, `"Pentatonic Major"`. To handle spaces in the file names and to avoid the use of a dictionary, we use underscores `_` in the file name to identify a space. Same goes for selecting the scale name via a `StepPlayer`. Therefore, `StepPlayer(numsteps, "Custom Pentatonic_Major", key_of_scale)` finds the file: `pentatonic_major.yml`. 

For file contents, here's an example:
```yaml
name: 'Major'
range: 1
octave: 4
ascending:
    C: 'C D E F G A B'
```
- name: <String> Name of the Scale
- range: <Integer> How many octaves to play
- octave: <Integer> 1 = lowest, 9 = highest
- ascending: You are going to have a field per key of the scale. Make sure the final note in each key isn't the starting key; the program takes care of that for you. 



