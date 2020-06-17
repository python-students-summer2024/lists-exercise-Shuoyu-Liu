# Mood Assessor

Create an app whereby a user can enter their mood every day, and the program will diagnose any mood disorders detected over the course of the last week (7 days).

_Please note that this application is for educational and fun purposes only. It is intentionally simplistic, and does not attempt to accurately diagnose moods or psychiatric conditions._

## Requirements

You will create one function named `assess_mood()` in a file named `mood_assessor.py`, which performs the following tasks. Running this file directly will do nothing. You will call this function from a file named `main.py` - running `main.py` is how the program should be run.

You are welcome to break up the code into multiple funcitons within the `mood_assessor.py` file, as you have learned to do. But it must be possible to call only `assess_mood()` from `main.py` and have the entire program run from start-to-finish, regardless of how many other functions are called within `assess_mood()`.

### Asking for a mood entry

Every day the program is run, it should do the following once:

1. ask the user to input their mood
1. validate the user's response (the code must accept the following moods: `happy`, `sad`, `angry`, and `apathetic` moods)
1. if the response was invalid, repeat starting from step 1 until valid response is gathered
1. translate the user's response to an integer (`happy` -> 2, `relaxed` -> 1, `apathetic` -> 0, `sad` -> -1, `angry` -> -2)
1. store the integer as a new line in a text file named `mood_diary.txt` within a subdirectory named `data`.

### Limit input to once-per-day

If the user has already entered a valid mood on any given day, and the user attempts to run the program again on that same day, the program must simply print, "Sorry, you have already entered your mood today." and quit.

You are free to do this any way you wish. You may find the `datetime` module useful in determining the current date.

### Diagnosing disorders

The first time the program is run each day, after gathering the mood from the user according to the instructions above, the program should also do the following:

1. check whether there are at least 7 entries in the `mood_diary.txt` file.
1. if not, do nothing further.
1. if so, retrieve the most recent 7 entries from the `mood_diary.txt` text file (i.e. the last 7 lines)
1. calculate the average mood from those entries (take the rounded numeric average of the 7 entries, and convert that to the appropriate string representing a mood.)
1. if the user has been happy for 5 or more days out of the last 7 days, the user should be diagnosed as `manic`
1. if the user has been sad for 4 or more days out of the last 7, the user should be diagnosed as `depressive`
1. if the user has been apathetic for 6 or more days out of the last 7, the user should be diagnosed as `schizoid`
1. if none of the above apply, then simply output the user's average (or most frequent) mood over the last six days

## Clone this repository

First, clone this repository to your local computer, using Visual Studio Code's cloning feature.

Helpful video:

- [cloning a code repository from GitHub to your local machine](https://www.youtube.com/watch?v=axcny0o1NYo).

## Set up Visual Studio Code

Once cloned, set Visual Studio Code to be suitable for Python development using the "command palette":

- set the interpreter to a Python 3.x interpreter, such as that by [`Anaconda`](https://www.anaconda.com/).
- set the linter to by `pylint`.
- set the test framework to be `pytest`.

Helpful video:

- [Setting up Visual Studio Code for Python development](https://www.youtube.com/watch?v=xsXMzyK1M4I)

## Create the code

You must create three files:

- `mood_assessor.py` - this file must include a function named `assess_mood()` that takes no arguments and outputs the user's mood, based on the data found in the file named `mood_diary.txt`.
- `main.py` - this file must call the `assess_mood()` function defined in the file named `mood_assessor.py`.
- `data` / `mood_diary.txt` - this file must be automatically created by your program. It will store the user's mood entries.