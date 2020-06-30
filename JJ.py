import mido
import sys
from midi2audio import FluidSynth

mid = mido.MidiFile()
track1 = mido.MidiTrack()
track2 = mido.MidiTrack()
track3 = mido.MidiTrack()
track4 = mido.MidiTrack()
track5 = mido.MidiTrack()
track6 = mido.MidiTrack()
mid.tracks.append(track1)
mid.tracks.append(track2)
mid.tracks.append(track3)
mid.tracks.append(track4)
mid.tracks.append(track5)
mid.tracks.append(track6)
tra = [track1,track2,track3,track4,track5,track6]

ins = 0

#bpm = \frac{60000000}{tempo}
def music1(note,base_num,base_time):
    if note==1.5:
        base_note = 60#+12
        track1.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60#+12
        track1.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60#+12
        track1.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60#+12
        track1.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60#+12
        track1.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60#+12
        track1.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))


def music2(note,base_num,base_time):
    if note==1.5:
        base_note = 60#+12
        track2.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60#+12
        track2.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60#+12
        track2.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60#+12
        track2.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60#+12
        track2.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60#+12
        track2.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))
     

def music3(note,base_num,base_time):
    if note==1.5:
        base_note = 60#+12
        track3.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60#+12
        track3.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60#+12
        track3.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60#+12
        track3.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60#+12
        track3.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60#+12
        track3.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))


def music4(note,base_num,base_time):
    if note==1.5:
        base_note = 60#+12
        track4.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60#+12
        track4.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60#+12
        track4.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60#+12
        track4.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60#+12
        track4.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60#+12
        track4.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))

def music5(note,base_num,base_time):
    if note==1.5:
        base_note = 60#+12
        track5.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60#+12
        track5.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60#+12
        track5.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60#+12
        track5.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60#+12
        track5.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60#+12
        track5.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))


def music6(note,base_num,base_time):
    if note==1.5:
        base_note = 60+12
        track6.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60+12
        track6.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60+12
        track6.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60+12
        track6.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60+12
        track6.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))    
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60+12
        track6.append(mido.Message('program_change',channel=0,program=ins,time=0))
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))

y1=[0,1,5,3,
3,1,5,3,
6,1,5,3,5,
5,6,1,2,4,3,
1,1,5,3,
3,1,5,3,
6,1,5,3,5,
5,6,1,2,1,
0,5,3,5,5,6,7,
2,2,2,3,3,5,6,
1,6,1,6,1,2,
2.5,2.5,1,5.5,5.5,4,5,
5,3,5,5,6,7,
2,2,2,3,3,6,1,
6,1,6,1,2,
2.5,2.5,1,5,
6,1,5,6,1,1,2,
7,0,5,
6,1,5,6,1,1,6,
2,0,5,
5,5,5,
0,3,5,3,5,4,3,7,
3,5,3,5,4,3,1,
3,5,3,5,6,1,
1,5.5,1,5.5,4,3,1,4,3,1,
3,5,3,5,4,3,7,
3,5,3,5,4,3,1,
3,5,6,1,2,3,
4,3,4,3,4,3,4,3,1,2,
1,1,5,3,
7,1,5,7,2,
1,5,3,
6,4,3,1,
0,5,3,5,3,5,6,
7,2,2,2,3,3,5,6,
1,6,1,6,1,2,
2.5,2.5,1,5.5,5.5,4,5,
5,3,5,3,5,6,7,
2,2,2,3,3,6,1,
6,1,0,6,1,2,
2.5,2.5,1,2,5,
6,1,5,6,1,1,2,7,
6,5,5,
6,1,6,1,6,1,2,
5,3,4,2,3,2,1,
3,5,3,5,4,3,7,
3,5,3,5,4,3,
1,3,5,3,5,6,1,
1,5.5,1,4,3,1,4,3,1,2,
1,3,5,3,5,4,3,
7,3,5,3,5,4,3,
1,3,5,6,1,2,3,
4,3,4,3,4,3,4,3,1,2,
1,1,5,3,
7,1,5,7,2,
1,
5,
0,6,1,2,3,2,1,1,2,
3,2,1,1,2,3,5,5,
0,1,2,2.5,2,1,1,5,
5.5,5,6.5,5.5,5.5,5.5,4,5,
0,3,5,3,5,4,3,7,
3,5,3,5,4,3,1,
0,3,5,3,5,6,1,
1,1,5,4,3,1,4,3,1,1,
6,5,3,5,3,5,4,3,
7,3,5,3,5,4,3,
1,3,5,6,1,2,3,
4,3,4,3,4,3,4,3,1,2,
1,
7,7,2,
1,
5,
3,1,7,1,3,1,7,1,3,1,7,1,3,1,7,1,
3,1,7,1,3,1,7,1,7,2,
1,
3,1,7,1,3,1,7,1,5
]

d1=[0,3,2,2,
-2,3,2,2,
-2,3,2,2,2,
2,2,2,2,2,2,
-2,2,2,2,
-2,3,2,2,
-2,3,2,2,2,
2,2,2,2,2,
0,0,0,0,0,0,0,
1,1,1,1,1,0,0,
1,0,1,0,1,1,
1,1,1,0,0,0,0,
0,0,0,0,0,0,
1,1,1,1,1,0,1,
0,1,0,1,1,
1,1,1,0,
0,1,0,0,1,1,1,
0,0,0,
0,1,0,0,1,1,0,
1,0,0,
0,0,0,
0,1,1,1,1,1,1,0,
1,1,1,1,1,1,1,
1,1,1,1,1,1,
1,0,1,0,1,1,1,1,1,1,
1,1,1,1,1,1,0,
1,1,1,1,1,1,1,
1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,2,1,1,
0,2,1,0,1,
1,1,1,
0,1,1,1,
0,0,0,0,0,0,0,
0,1,1,1,1,1,0,0,
1,0,1,0,1,1,
1,1,1,0,0,0,0,
0,0,0,0,0,0,0,
1,1,1,1,1,0,1,
0,1,0,0,1,1,
1,1,1,1,0,
0,1,0,0,1,1,1,0,
0,0,0,
0,1,0,1,0,1,1,
1,1,1,1,1,1,1,
1,1,1,1,1,1,0,
1,1,1,1,1,1,
1,1,1,1,1,1,1,
1,0,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,
0,1,1,1,1,1,1,
1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,2,1,1,
0,2,1,0,1,
1,
0,
0,0,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,
0,1,1,1,1,1,1,0,
1,1,1,1,1,1,1,1,
0,1,1,1,1,1,1,0,
1,1,1,1,1,1,1,
0,1,1,1,1,1,1,
1,1,0,1,1,1,1,1,1,1,
0,0,1,1,1,1,1,1,
0,1,1,1,1,1,1,
1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,
0,0,1,
1,
1,
2,2,1,2,2,2,1,2,2,2,1,2,2,2,1,2,
2,2,1,2,2,2,1,2,0,1,
1,
1,1,0,1,1,1,0,1,0]

t1=[1,1,1,1,
1,1,1,1,
1,1,1,0.5,0.5,
0.5,0.5,1,1,0.5,0.5,
1,1,1,1,
1,1,1,1,
1,1,1,0.5,0.5,
0.5,0.5,1,1,1,
1,0.5,0.5,1,0.25,0.5,1.25,
0.25,0.75,0.5,0.5,0.5,0.25,1.25,
0.5,0.25,1,0.25,0.5,0.5,
0.5,0.5,1,0.5,1,0.25,1.25,
0.5,0.5,1,0.25,0.5,1.25,
0.25,0.75,0.25,0.75,0.5,0.25,1.75,
0.5,1.25,0.25,0.25,0.25,
1,0.5,2,0.5,
0.25,1.5,0.25,0.25,0.75,0.5,0.5,
3,0.5,0.5,
0.5,1.25,0.25,0.25,0.75,0.5,0.5,
3,0.5,0.5,
1,1,2,
1,0.25,0.75,0.25,0.75,0.25,0.5,1.25,
0.25,0.75,0.25,0.75,0.25,0.5,1.25,
0.5,0.5,0.25,0.75,0.5,0.5,
0.5,0.25,1,0.25,0.5,0.5,0.5,0.5,0.5,1.5,
0.25,0.75,0.25,0.75,0.25,0.5,1.25,
0.25,0.75,0.25,0.75,0.25,0.5,1.25,
0.25,0.5,0.75,0.25,0.5,0.75,
0.25,0.5,0.25,0.5,0.25,0.5,0.25,0.25,0.25,1,
1,1,1,1,
1,1,1,0.5,1.5,
1,1,1,
3,0.25,0.25,0.5,
1,0.5,0.5,0.5,0.5,0.25,0.75,
1,0.25,0.75,0.5,0.5,0.5,0.25,1.25,
0.5,0.25,0.75,0.25,0.75,0.5,
0.5,0.5,1,0.5,1,0.25,1.25,
0.5,0.5,0.5,0.5,0.25,0.5,1.25,
0.25,0.75,0.5,0.5,0.5,0.25,1.5,
0.5,1,0.25,0.25,0.25,0.25,
1,0.5,1,1,0.5,
0.5,1.25,0.25,0.25,0.75,0.5,0.25,1.5,
0.25,1.75,0.5,
0.5,1.25,0.25,0.5,0.5,0.5,0.5,
0.5,1,0.25,1.25,0.5,0.25,1.25,
0.25,0.75,0.25,0.75,0.5,0.25,1.25,
0.25,0.75,0.25,0.75,0.25,0.75,
1,0.5,0.5,0.25,0.5,0.75,1,
0.5,0.25,1.25,0.25,0.25,0.25,0.25,0.25,0.25,1,
0.5,0.25,0.75,0.25,0.75,0.5,0.5,
1,0.25,0.75,0.25,0.75,0.5,0.5,
1,0.25,0.5,0.75,0.25,0.5,0.75,
0.25,0.5,0.25,0.5,0.25,0.5,0.25,0.25,0.25,1,
1,1,1,1,
1,1,1,0.5,1,
3.5,
4,
0.5,0.5,0.5,0.5,0.25,0.25,0.5,0.5,0.5,
0.25,0.25,0.5,0.5,0.5,0.5,0.25,1.25,
1,0.5,0.5,0.25,0.25,0.5,0.5,0.5,
0.5,1,0.5,0.5,0.25,0.25,0.25,2.75,
1,0.5,0.5,0.25,0.75,0.5,0.25,1.25,
0.5,0.5,0.25,0.75,0.25,0.5,0.75,
0.5,0.25,0.75,0.5,0.5,0.5,0.5,
0.75,1,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.75,
0.25,0.5,0.25,0.75,0.25,0.75,0.25,0.75,
1,0.5,0.5,0.25,0.75,0.5,0.5,
1,0.25,0.5,0.75,0.5,0.25,0.75,
0.25,0.5,0.25,0.5,0.25,0.5,0.25,0.25,0.25,1.5,
3.5,
2.5,0.5,1.5,
3.5,
4,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,1.5,
4,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,2
]


y2=[3,1,7,1,3,1,7,1,3,1,7,1,3,1,7,1,
3,1,7,1,3,1,7,1,3,1,7,1,3,1,7,1,
3,1,7,1,3,1,7,1,3,1,7,1,3,
4,1,4,6,4,
3,1,7,1,3,1,7,1,3,1,7,1,3,1,7,1,
3,1,7,1,3,1,7,1,3,1,7,1,3,1,7,1,
3,1,7,1,3,1,7,1,3,1,7,1,3,1,7,1,
4,1,4,
1,5,1,3,5,
3,7,3,5,7,
6,3,6,3,1,
4,1,4,5.5,1,
1,5,1,5,1,
7,5,7,5,3,
6,3,6,3,1,3,
4,1,4,1,5.5,
2,6,2,4,6,
5,2,5,2,7,2,
2,6,2,4,6,
5,2,5,2,7,2,5,2,
5,
1,1,1,1,
3,7,7,7,
6,6,6,6,
4,4,5.5,5,
1,1,1,1,
3,7,7,7,
6,6,6,6,
4,4,5,5,
1,5,1,5,3,
3,7,3,7,5,
6,3,6,3,1,
4,1,4,1,6,
1,5,1,5,3,5,1,5,
3,7,3,7,5,7,3,7,
6,3,6,3,1,3,6,3,
4,1,4,1,5.5,1,4,1,
1,5,1,5,3,5,1,5,
3,7,3,7,5,7,3,7,
6,3,6,3,1,3,6,3,
4,1,4,1,5.5,1,4,1,
2,6,2,6,4,6,2,6,
5,2,5,2,7,2,5,2,
2,6,2,6,4,6,2,6,
5,2,5,2,7,
1,5,1,5,3,5,1,5,
3,7,3,7,5,7,3,7,
6,3,6,3,1,3,6,3,
4,1,5.5,5,2,5.5,
1,5,1,5,3,5,1,5,
3,7,3,7,5,7,3,7,
6,3,6,3,1,3,6,3,
4,1,4,5,2,5,
1,5,1,5,3,5,1,5,
3,7,3,7,5,7,3,7,
6,3,6,3,1,3,6,3,
4,1,4,1,5,2,5,2,
2,2,2,2,
3,3,3,3,
4,4,4,4,
5.5,2.5,5.5,2,5.5,2.5,5.5,2,5,
1,5,1,1,1,
7,5,7,7,7,
6,3,1,1,1,
4,1,4,
1,5,1,5,3,5,1,5,
3,7,3,7,5,7,3,7,
6,3,6,3,1,3,6,3,
4,1,6,5,2,7,
1,5,1,5,3,5,1,5,
3,7,3,5,7,3,5,
6,3,6,3,1,3,6,3,
4,1,4,1,6,1,4,
1,2,
3,
3,1,7,1,3,1,7,1,3,1,7,1,3,1,7,1,
4,1,4,5
]

d2=[0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,
0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,
0,0,-1,0,0,0,-1,0,0,0,-1,0,0,
-1,0,0,0,0,
0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,
0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,
0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,
-1,0,0,
-2,-2,-1,-1,-1,
-2,-2,-1,-1,-1,
-2,-1,-1,-1,0,
-2,-1,-1,-1,0,
-1,-1,0,-1,0,
-2,-1,-1,-1,0,
-2,-1,-1,-1,0,-1,
-2,-1,-1,-1,-1,
-2,-2,-1,-1,-1,
-2,-1,-1,-1,-1,-1,
-2,-2,-1,-1,-1,
-2,-1,-1,-1,-1,-1,-1,-1,
-2,
-1,0,0,0,
-2,-1,-1,-1,
-2,-1,-1,-1,
-1,-1,-1,-1,
-1,0,0,0,
-1,-1,-1,-1,
-2,-1,-1,-1,
-1,-1,-1,-1,
-1,-1,0,-1,0,
-1,-1,0,-1,0,
-2,-1,-1,-1,0,
-2,-1,-1,-1,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,0,-1,-1,-1,
-2,-1,-1,-1,-1,-1,-1,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,0,-1,-1,-1,
-2,-1,-1,-1,-1,-1,-1,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,-1,-1,-1,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,-1,
-1,-1,0,-1,0,-1,0,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,0,-1,-1,-1,
-2,-1,-1,-2,-1,-1,
-1,-1,0,-1,0,-1,0,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,0,-1,-1,-1,
-2,-1,-1,-2,-1,-1,
-1,-1,0,-1,0,-1,0,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,0,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-1,-1,-1,
-2,-1,-1,-1,
-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,-2,
-1,-1,0,0,0,
-2,-1,-1,-1,-1,
-2,-1,0,0,0,
-1,0,0,
-1,-1,0,-1,0,-1,0,-1,
-2,-2,-1,-2,-1,-2,-1,-2,
-2,-1,-1,-1,0,-1,-1,-1,
-2,-1,-1,-2,-1,-1,
-1,-1,0,-1,0,-1,0,-1,
-2,-2,-1,-1,-1,0,0,
-2,-1,-1,-1,0,-1,-1,-1,
-2,-1,-1,-1,-1,-1,-1,
-2,-2,
-2,
0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,
-2,-1,-1,-2]

t2=[0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,1,
0.5,0.5,0.5,0.5,2,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
0.5,0.5,3,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,1,1,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,1,1,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
4,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
1,1,1,1,
1,1,1,1,
1,1,1,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,2,
0.5,0.5,1,1,1,
0.5,0.5,1,1,1,
0.5,0.5,1,1,1,
0.5,0.5,3,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,1,
3,1,
4,
0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
0.5,0.5,1,2
]

print((len(y2),len(d2),len(t2)))

y3=[5,3,3,3,
7,3,3,3,
3,1,1,1,
5.5,5,2,2,
5,3,3,3,
7,3,3,3,
3,1,1,1,
1,1,2,2]

d3=[-1,0,0,0,
-2,0,0,0,
-2,0,0,0,
-1,-1,0,0,
-1,0,0,0,
-1,0,0,0,
-1,0,0,0,
0,0,0,0,
]

t3=[1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1
]

y4=[0,5,5,5,
0,5,5,5,
0,3,3,3,
1,1,5,5,
0,5,5,5,
0,5,5,5,
0,3,3,3,
4,4,5,5]

d4=[0,0,0,0,
0,0,0,0,
0,0,0,0,
0,0,0,0,
0,0,0,0,
0,0,0,0,
0,0,0,0,
0,0,0,0
]

t4=[1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1]

i=0
while i<len(y1):
    music1(y1[i],d1[i],t1[i])
    i=i+1

i=0
while i<len(y2):
    music2(y2[i],d2[i],t2[i])
    i=i+1

for i in range(0,21):
    music3(0,0,4)
    music4(0,0,4)

i=0
while i<len(y3):
    music3(y3[i],d3[i],t3[i])
    music4(y4[i],d4[i],t4[i])
    i=i+1

for i in range(0,28):
    music3(0,0,4)

yy3=[2,6,6,6,
3,1,1,1,
4,5.5,5,5]
dd3=[-1,-1,-1,-1,
-1,0,0,0,
-1,-1,-1,-1]
tt3=[1,1,1,1,
1,1,1,1,
1,1,1,1]
i=0
while i<len(yy3):
    music3(yy3[i],dd3[i],tt3[i])
    i=i+1

music3(0,0,15*4+6+2)
music3(2,1,2)
music4(0,0,46*4+6+2)
music4(1,1,2)

mid.save("F:\\VSCODE\\music\\不为谁而作的歌（钢琴）.mid")

#FluidSynth().midi_to_audio("F:\\VSCODE\\music\\不为谁而作的歌（钢琴）.mid", "F:\\VSCODE\\music\\不为谁而作的歌（钢琴）.wav")