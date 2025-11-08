import sys
import time
import random

def type_out(text, min_speed= 0.02, max_speed=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        delay = random.uniform(min_speed, max_speed)
        time.sleep(delay)
    print()

type_out('Wake up, Neo.\nThe Matrix has you.')
time.sleep(2)

type_out('Take the blue pill or the red pill.\n')
time.sleep(0.5)
type_out('If you take the blue pill:\nYou blink and wake up in your bed. The morning light spills through the blinds.\
         \nEverything feels normal.')
time.sleep(0.5)
type_out('But deep down, something feels wrong... like a dream you cannot quite remember.')

type_out('Want to know about the red pill?')
answer = input().lower()
if answer in ['yes' or 'sure' or 'yeah']:
    type_out('Good boy.')
elif answer in ['no' or 'nah']:
    type_out('Well too bad.')
else:
    type_out('Did not understand your response. Anyways, lets talk about the red pill')

type_out('If you take the red pill:\
\nYour vision fractures. The world dissolves into lines of green code.\
\nYou wake up gasping inside a dark pod filled with liquid.')

type_out('Which is it gonna be? (blue/red)')
pill = input('> ').lower()

if pill == 'blue':
    type_out('\nYou open your eyes. The alarm clock blinks 7:00 a.m. Everything feels... soft, familiar.\n')
    type_out('You sit up, uneasy. Do you go to work or check your computer?')
    choice1 = input('> ').lower()

    if 'work' in choice1:
        type_out('\nYou step outside. The air feels heavy. On the subway, no one makes eye contact.\n')
        type_out('When you arrive, a message is waiting on your desk: "Wake up, Neo."')
        time.sleep(1)
        type_out('\nDo you open it or throw it away?')
        choice2 = input('> ').lower()

        if 'open' in choice2:
            type_out('\nThe screen flickers. You see your own face on a security feed. Someone whispers, "They’re watching you."')
        else:
            type_out('\nYou ignore it. But the moment you look away, the lights go out. Total darkness. You feel something breathing behind you...')

    elif 'computer' in choice1:
        type_out('\nYou sit down at your computer. The screen turns black and green text starts typing itself.\n')
        type_out('"Do you want to see the truth?"')
        choice2 = input('> ').lower()

        if 'yes' in choice2:
            type_out('\nA surge of static fills your head. For a moment, you see the Matrix’s code pulsing behind the walls.')
            type_out('You scream, but no sound comes out.')
        else:
            type_out('\nThe monitor explodes into a blinding white flash. When your vision returns, the world outside your window has frozen completely.')

elif pill == 'red':
    type_out('\nYou swallow the pill. The walls dissolve into streams of code. You wake up suspended in liquid.\n')
    type_out('A voice echoes: "Follow my voice... or find your own way."')
    choice1 = input('> ').lower()

    if 'follow' in choice1:
        type_out('\nYou crawl through the metal tunnel toward the voice. A hatch opens, revealing a man in a long black coat.\n')
        type_out('"You’re not ready yet," he says. "But you will be."')
        time.sleep(1)
        type_out('He offers you a choice: Join him or run.')
        choice2 = input('> ').lower()

        if 'join' in choice2:
            type_out('\nHe smiles faintly. "Welcome to Zion." A blinding light consumes your vision.')
        else:
            type_out('\nYou turn and run into the darkness. The machines stir. Metal claws screech from the walls. There’s no escape.')

    elif 'find' in choice1 or 'explore' in choice1:
        type_out('\nYou drift through corridors lined with pods. Millions of humans still asleep.\n')
        type_out('You spot a maintenance hatch. Do you open it or ignore it?')
        choice2 = input('> ').lower()

        if 'open' in choice2:
            type_out('\nYou slip inside. A pulse of heat rushes through the pipes. You find an unplugged terminal humming quietly...')
            type_out('"Someone has been here before you."')
        else:
            type_out('\nYou keep walking. The air thickens. One by one, the pods begin to open. Eyes stare back at you — awake, terrified.')

else:
    type_out('\nYou hesitate. The system glitches.\n')
    type_out('The pills vanish, replaced by a mirror. Your reflection looks back and smiles.\n')
    type_out('"You were never given a choice," it says.\n')
    type_out('The world folds in on itself.')

time.sleep(1)
type_out('Talk soon...')