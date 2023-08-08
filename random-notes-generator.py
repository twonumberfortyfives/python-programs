import random
import midiutil
from midiutil import MIDIFile

# Create a new MIDIFile object with one track
MyMIDI = MIDIFile(1)

# Define a musical scale using intervals
scale = [0, 2, 4, 5, 7, 9, 11]

# Define minimum and maximum MIDI note values
min_note = 36
max_note = 84

# Define the number of notes to generate
num_notes = 100

# A list to store the generated notes
generated_notes = []

# Generate random notes and add them to the 'generated_notes' list
for i in range(num_notes):
    # Generate a random MIDI note value
    random_height = random.randint(0, 100)

    # Adjust the random note to fit within the defined scale
    while random_height % 12 not in scale:
        random_height -= 1
    while random_height < 36:
        random_height += 12
    while random_height > 84:
        random_height -= 12

    # Check if the generated note is outside the defined range and adjust it
    if random_height < min_note:
        generated_notes.append((min_note, random_height, False))
        random_height = min_note
    elif random_height > max_note:
        generated_notes.append((max_note, random_height, False))
        random_height = max_note

    # Append the generated note to the list with a flag indicating it's valid
    generated_notes.append((random_height, random_height, True))

# Print the generated valid notes
for note, original_note, flag in generated_notes:
    if flag:
        print(note, end=" ")

# Save the generated notes as a MIDI file named "nuotit.mid"
with open("./nuotit.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
