"""Repeating a beat in a loop."""

__author__ = "730395734"

counter: int = 0
beat_input: str = input("What beat do you want to repeat? ")
maximum: int = int(input("How many times do you want to repeat it? "))

while counter < maximum:
    print(beat_input * maximum)
    if counter >= maximum:
        print("No beat...")