import mido
import sys


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

#bpm = \frac{60000000}{tempo}
def music1(note,base_num,base_time):
    if note==1.5:
        base_note = 60+12
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60+12
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60+12
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60+12
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60+12
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60+12
        track1.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track1.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))


def music2(note,base_num,base_time):
    if note==1.5:
        base_note = 60+12
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60+12
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60+12
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60+12
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60+12
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60+12
        track2.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track2.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))
     

def music3(note,base_num,base_time):
    if note==1.5:
        base_note = 60+12
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60+12
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60+12
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60+12
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60+12
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60+12
        track3.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track3.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))


def music4(note,base_num,base_time):
    if note==1.5:
        base_note = 60+12
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60+12
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60+12
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60+12
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60+12
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60+12
        track4.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track4.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))

def music5(note,base_num,base_time):
    if note==1.5:
        base_note = 60+12
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60+12
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60+12
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60+12
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60+12
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60+12
        track5.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track5.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))


def music6(note,base_num,base_time):
    if note==1.5:
        base_note = 60+12
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 1, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 1, velocity=96, time=int(720*base_time),channel=0))
    elif note==2.5:
        base_note = 60+12
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 3, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 3, velocity=96, time=int(720*base_time),channel=0))
    elif note==4.5:
        base_note = 60+12
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 6, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 6, velocity=96, time=int(720*base_time),channel=0))
    elif note==5.5:
        base_note = 60+12
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 8, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 8, velocity=96, time=int(720*base_time),channel=0))
    elif note==6.5:
        base_note = 60+12
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + 10, velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + 10, velocity=96, time=int(720*base_time),channel=0))    
    else:
        major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
        base_note = 60+12
        track6.append(mido.Message('note_on', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=0,channel=0))
        track6.append(mido.Message('note_off', note=base_note+base_num*12 + sum(major_notes[0:note]), velocity=96, time=int(720*base_time),channel=0))

yin1=[7,1,2,3,5,5,3,
7,1,2,3,5,5,3,2,3,1,2,7,1,5,
7,1,2,3,5,5,3,
7,1,2,3,5,5,3,2,3,1,2,7,1,5,
7,1,2,3,5,5,3,
7,1,2,3,5,5,3,2,3,1,2,7,1,5,
7,1,2,3,5,5,3,
6,6,
2,1,2,1,2,3,5,3,
2,1,2,1,2,3,2,1,5,
2,1,2,1,2,3,5,3,
2,3,2,1,2,
2,1,2,1,2,3,5,3,
2,3,2,1,6,3,2,1,2,
1,3,2,1,2,1,5,3,2,1,2,
1,1,2,3,1,
6,5,6,1,7,6,7,
7,6,7,3,1,2,1,7,6,5,
6,5,6,5,6,5,6,5,2,5,
3,1,2,3,1,
6,5,6,1,7,6,7,
3,6,7,3,1,2,1,7,6,5.5,#*,
6,3,3,5,6,3,3,5,6,
6,1,2,
3,6,5,6,5,6,5,2,3,
6,5,6,5,6,5,3,
2,1,6,1,6,2,1,6,1,
3,4,3,4,3,2,1,2,
3,6,5,6,5,6,5,2,
3,6,5,6,5,6,5,3,
2,1,6,3,2,1,6,1,
1,6,3,
2,1,6,3,2,1,6,1,
7,1,2,3,5,5,3,
7,1,2,3,5,5,3,2,3,1,2,7,1,5,
7,1,2,3,5,5,3,
6,6,
2,1,2,1,2,3,5,3,
2,1,2,1,2,3,2,1,5,
2,1,2,1,2,3,5,3,
2,3,2,1,2,
2,1,2,1,2,3,5,3,
2,3,2,1,6,3,2,1,2,
1,3,2,1,2,1,5,3,2,1,2,
1,1,2,3,1,
6,5,6,1,7,6,7,
7,6,7,3,1,2,1,7,6,5,
6,5,6,5,6,5,6,5,2,5,
3,1,2,3,1,
6,5,6,1,7,6,7,
3,6,7,3,1,2,1,7,6,5.5,#*,
6,3,3,5,6,3,3,5,6,
6,1,2,
3,6,5,6,5,6,5,2,3,
6,5,6,5,6,5,3,
2,1,6,1,6,2,1,6,1,
3,4,3,4,3,2,1,2,
3,6,5,6,5,6,5,2,
3,6,5,6,5,6,5,3,
2,1,6,3,2,1,6,1,
1,6,3,
2,1,6,3,2,1,6,1,
1,
7,1,2,3,5,5,3,
7,1,2,3,5,5,3,2,3,1,2,7,1,5,
7,1,2,3,5,5,3,
7,1,2,3,5,5,3,2,3,1,2,7,1,6,5,
]
diao1 = [-1,0,0,0,-1,0,0,
-1,0,0,0,-1,0,0,0,0,0,0,-1,0,-1,
-1,0,0,0,-1,0,0,
-1,0,0,0,-1,0,0,0,0,0,0,-1,0,-1,
-1,0,0,0,-1,0,0,
-1,0,0,0,-1,0,0,0,0,0,0,-1,0,-1,
-1,0,0,0,-1,0,0,
-1,-1,#
0,0,0,0,0,0,0,0,#
0,0,0,0,0,0,0,0,-1,#
0,0,0,0,0,0,0,0,
0,0,0,0,0,
0,0,0,0,0,0,0,0,#
0,0,0,0,-1,0,0,0,0,#
0,0,0,0,0,0,-1,0,0,0,0,#
0,0,0,0,0,
0,0,0,0,0,0,0,#
0,0,0,0,1,1,1,0,0,0,#
0,0,0,0,0,0,0,0,0,0,#
0,0,0,0,0,#
0,0,0,0,0,0,0,#
0,0,0,0,1,1,1,0,0,0,#
0,1,1,0,0,1,1,0,0,#
0,1,1,#
1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,
1,1,0,1,0,1,1,0,1,
1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,
1,1,0,1,1,1,0,1,
1,0,1,
1,1,0,1,1,1,0,1,
-1,0,0,0,-1,0,0,
-1,0,0,0,-1,0,0,0,0,0,0,-1,0,-1,
-1,0,0,0,-1,0,0,
-1,-1,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,-1,
0,0,0,0,0,0,0,0,
0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,-1,0,0,0,0,
0,0,0,0,0,0,-1,0,0,0,0,
0,0,0,0,0,
0,0,0,0,0,0,0,
0,0,0,0,1,1,1,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,
0,0,0,0,0,0,0,
0,0,0,0,1,1,1,0,0,0,
0,1,1,0,0,1,1,0,0,
0,1,1,
1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,
1,1,0,1,0,1,1,0,1,
1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,
1,1,0,1,1,1,0,1,
1,0,1,
1,1,0,1,1,1,0,1,
1,
0,1,1,1,0,1,1,
0,1,1,1,0,1,1,1,1,1,1,0,1,0,
0,1,1,1,0,1,1,
0,1,1,1,0,1,1,1,1,1,1,0,1,0,0
]
time1 = [0.25,0.25,0.25,0.5,0.25,0.25,2.25,
0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
2,2,
0.75,0.25,0.75,0.25,0.5,0.5,0.5,0.5,
0.75,0.25,0.75,0.25,0.25,0.25,0.25,0.25,1,
0.75,0.25,0.75,0.25,0.5,0.5,0.5,0.5,
0.75,0.25,0.5,0.5,2,
0.75,0.25,0.75,0.25,0.5,0.5,0.5,0.5,
0.75,0.25,0.5,0.5,1,0.25,0.25,0.25,0.25,
1,0.25,0.25,0.25,0.25,0.75,0.25,0.25,0.25,0.25,0.25,
2,0.5,0.5,0.5,0.5,
0.5,0.25,1,0.25,0.5,0.25,1.25,
0.5,0.25,0.75,0.5,0.25,0.25,0.25,0.25,0.5,0.5,
0.5,0.25,0.5,0.25,0.25,0.25,0.5,0.25,0.5,0.75,
2,0.5,0.5,0.5,0.5,
0.5,0.25,1,0.25,0.5,0.25,1.25,
0.5,0.25,0.75,0.5,0.25,0.25,0.25,0.25,0.5,0.5,
0.5,0.25,0.75,0.5,0.5,0.25,0.5,0.5,0.25,
3,0.5,0.5,
0.5,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,
0.25,0.75,0.25,0.75,0.25,0.5,0.75,
0.5,0.25,0.5,0.5,0.25,0.5,0.25,0.5,0.75,
1.25,0.25,0.25,0.125,0.125,1,0.5,0.5,
0.5,0.25,0.75,0.25,0.75,0.25,0.75,0.5,
0.5,0.25,0.75,0.25,0.75,0.25,0.5,0.75,
0.5,0.25,0.5,0.75,0.5,0.25,0.5,0.75,
3,0.25,0.75,
0.5,0.25,0.5,0.75,0.5,0.25,0.5,0.75,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
2,2,0.75,0.25,0.75,0.25,0.5,0.5,0.5,0.5,
0.75,0.25,0.75,0.25,0.25,0.25,0.25,0.25,1,
0.75,0.25,0.75,0.25,0.5,0.5,0.5,0.5,
0.75,0.25,0.5,0.5,2,
0.75,0.25,0.75,0.25,0.5,0.5,0.5,0.5,
0.75,0.25,0.5,0.5,1,0.25,0.25,0.25,0.25,
1,0.25,0.25,0.25,0.25,0.75,0.25,0.25,0.25,0.25,0.25,
2,0.5,0.5,0.5,0.5,
0.5,0.25,1,0.25,0.5,0.25,1.25,
0.5,0.25,0.75,0.5,0.25,0.25,0.25,0.25,0.5,0.5,
0.5,0.25,0.5,0.25,0.25,0.25,0.5,0.25,0.5,0.75,
2,0.5,0.5,0.5,0.5,
0.5,0.25,1,0.25,0.5,0.25,1.25,
0.5,0.25,0.75,0.5,0.25,0.25,0.25,0.25,0.5,0.5,
0.5,0.25,0.75,0.5,0.5,0.25,0.5,0.5,0.25,
3,0.5,0.5,
0.5,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,
0.25,0.75,0.25,0.75,0.25,0.5,0.75,
0.5,0.25,0.5,0.5,0.25,0.5,0.25,0.5,0.75,
1.25,0.25,0.25,0.125,0.125,1,0.5,0.5,
0.5,0.25,0.75,0.25,0.75,0.25,0.75,0.5,
0.5,0.25,0.75,0.25,0.75,0.25,0.5,0.75,
0.5,0.25,0.5,0.75,0.5,0.25,0.5,0.75,
3,0.25,0.75,
0.5,0.25,0.5,0.75,0.5,0.25,0.5,0.75,
4,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,4.25
]

yin2 = [4,1,3,5,7,2,
3,7,2,6,1,3,
4,1,3,5,7,2,
3,7,2,6,1,3,
4,1,3,5,7,2,
3,7,2,6,1,3,
4,1,3,5,7,2,
6,6,
1,5,1,5,5,1,5,
7,5,7,5,
6.5,5,6.5,5,5,6,5,
4,1,4,1,4,
2,6,2,6,5,2,5,2,
6,3,6,3,6,
4,1,4,1,5,2,5,2,
1,5,1,5,1,
4,1,4,1,5,2,5,2,
3,7,3,7,6,3,6,3,
4,1,4,1,5,2,5,2,
1,5,1,5,6.5,5,
4,1,4,1,5,2,5,2,
3,5.5,6,3,6,3,
4,1,4,1,5,2,5,2,
6,6,6,6,6,6,6,6,
4,1,4,1,5,2,5,2,
3,7,3,7,6,3,6,3,
4,1,4,1,5,2,5,2,
1,5,1,5,3,5.5,
4,1,4,1,5,2,5,2,
3,7,3,7,6,3,6,3,
4,1,4,1,4,2,5,2,
6,3,6,3,1,
4,1,4,1,5,2,5,2,
4,1,3,5,7,2,
3,7,2,6,1,3,
6,1,3,5,7,2,
6,6,
1,5,1,5,5,1,5,
7,5,7,5,
6.5,5,6.5,5,5,6,5,
4,1,4,1,4,
2,6,2,6,5,2,5,2,
6,3,6,3,6,
4,1,4,1,5,2,5,2,
1,5,1,5,1,
4,1,4,1,5,2,5,2,
3,7,3,7,6,3,6,3,
4,1,4,1,5,2,5,2,
1,5,1,5,6.5,5,
4,1,4,1,5,2,5,2,
3,5.5,6,3,6,3,
4,1,4,1,5,2,5,2,
6,6,6,6,6,6,6,6,
4,1,4,1,5,2,5,2,
3,7,3,7,6,3,6,3,
4,1,4,1,5,2,5,2,
1,5,1,5,3,5.5,
4,1,4,1,5,2,5,2,
3,7,3,7,6,3,6,3,
4,1,4,1,5,2,5,2,
6,3,6,3,1,
4,1,4,5,2,5,
1,5,2,2,
4,1,3,5,7,2,
3,7,2,6,1,3,
4,1,3,5,7,2,
3,7,2,6,1,3]


diao2 = [-2,-1,-1,-2,-2,-1,
-2,-2,-1,-2,-1,-1,
-2,-1,-1,-2,-2,-1,
-2,-2,-1,-2,-1,-1,
-2,-1,-1,-2,-2,-1,
-2,-2,-1,-2,-1,-1,
-2,-1,-1,-2,-2,-1,
-2,-2,
-1,-1,0,-1,-1,0,-1,
-2,-1,-1,-1,
-2,-1,-1,-1,-1,-1,-1,
-2,-1,-1,-1,-2,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-1,-1,0,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-1,-1,0,-1,-2,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-2,-2,-2,-2,-2,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-1,-1,0,-1,-2,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-1,-1,-1,0,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-1,-1,-2,-2,-1,
-2,-2,-1,-2,-1,-1,
-2,-1,-1,-2,-2,-1,
-2,-2,
-1,-1,0,-1,-1,0,-1,
-2,-1,-1,-1,
-2,-1,-1,-1,-1,-1,-1,
-2,-1,-1,-1,-2,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-1,-1,0,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-1,-1,0,-1,-2,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-2,-2,-2,-2,-2,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-1,-1,0,-1,-2,-2,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-2,-1,-2,-2,-1,-1,-1,
-2,-1,-1,-1,-2,-1,-1,-1,
-2,-1,-1,-1,0,
-2,-1,-1,-2,-1,-1,
-1,-1,0,0,
-2,-1,-1,-2,-2,-1,
-2,-2,-1,-2,-1,-1,
-2,-1,-1,-2,-2,-1,
-2,-2,-1,-2,-1,-1
]
time2 = [0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
2,2,
0.5,0.5,0.5,1,0.5,0.5,0.5,
0.5,0.5,0.5,2.5,
0.5,0.5,0.5,1,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,1,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
1,1,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,1,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
2,2,
0.5,0.5,0.5,1,0.5,0.5,0.5,
0.5,0.5,0.5,2.5,
0.5,0.5,0.5,1,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,1,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
1,1,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,1,1,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
0.5,0.5,0.5,0.5,2,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,2,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,1,
0.5,0.5,1,0.5,0.5,5
]

i=0
while i<len(diao1):
    music1(yin1[i],diao1[i],time1[i])
    i=i+1

i=0
while i<len(diao2):
    music2(yin2[i],diao2[i],time2[i])
    i=i+1

track3.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track3.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*16),channel=0))
yin3=[7,1,2,3,5,5,3,
7,1,2,3,5,5,3,2,3,1,2,7,1,5,
7,1,2,3,5,5,3,
2,1.5]
diao3=[0,1,1,1,0,1,1,
0,1,1,1,0,1,1,1,1,1,1,0,1,0,
0,1,1,1,0,1,1,
0,0]
time3=[0.25,0.25,0.25,0.5,0.25,0.25,2.25,
0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,
0.25,0.25,0.25,0.5,0.25,0.25,2.25,
2,2
]
i=0
while i<len(yin3):
    music3(yin3[i],diao3[i],time3[i])
    i=i+1

track3.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track3.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*13*4),channel=0))
music3(5.5,0,0.5)
track3.append(mido.Message('note_on', note=1, velocity=0, time=0,channel=0))
track3.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*11*4+720*3.5),channel=0))
i=0
while i<len(yin3):
    music3(yin3[i],diao3[i],time3[i])
    i=i+1
track3.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track3.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*13*4),channel=0))
music3(5.5,0,0.5)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*19*4+720*2),channel=0))
music4(6.5,-1,1)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*4+720*1),channel=0))
music4(3,-1,1)
music4(5.5,-1,1)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*4+720*2),channel=0))
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*3*4+720*2),channel=0))
music4(3,-1,1)
music4(5.5,-1,1)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*8*4),channel=0))
music4(3,-1,2)
music4(3,-1,2)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*11*4+720*2),channel=0))
music4(6.5,-1,1)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*4+720*1),channel=0))
music4(3,-1,1)
music4(5.5,-1,1)
track4.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track4.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*4+720*2),channel=0))
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
music4(3,-1,0.5)
track5.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track5.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*21*4),channel=0))
music5(7,0,0.5)
track5.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track5.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*11*4+720*3.5),channel=0))
music5(1,1,0.25)
track5.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track5.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*16*4+720*3.75),channel=0))
music5(7,0,0.5)
track6.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track6.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*23*4),channel=0))
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
track6.append(mido.Message('note_on', note= 1, velocity=0, time=0,channel=0))
track6.append(mido.Message('note_off', note= 1, velocity=0, time=int(720*21*4),channel=0))
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
music6(6,-1,0.5)
mid.save('ヤキモチ.mid')