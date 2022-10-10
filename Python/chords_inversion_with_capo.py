#this program will invert your guitar chord according to the fret you want to keep the capo in. Suppose your chord is C Major but you want to keep your capo in the 2nd fret, then the chord you will want to play after keeping the capo is D Major. So, the program will suggest you the same chord. You can invert many chords at the same time.

scales = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
capo_fret = int(input("Which fret do you want to keep the capo in? "))
no_of_chords = int(input("How many chords do you wanna invert? "))

init_chords = []
final_chords = []

for i in range(no_of_chords):
    init_chords.append(str(input("Enter the chord: ")))

print(init_chords)

for j in init_chords:
    final_chords.append(scales[scales.index(j) - capo_fret])

print(final_chords)
