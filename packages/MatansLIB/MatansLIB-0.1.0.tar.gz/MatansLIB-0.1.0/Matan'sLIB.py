import time
from pydub import AudioSegment
from pydub.playback import play

def play_audio(file_path):
    """Play an audio file."""
    sound = AudioSegment.from_file(file_path)
    play(sound)

def facto(num):
    """Calculate the factorial of a number."""
    if num == 0:
        return 1
    else:
        return num * facto(num-1)

def transfer(stri):
    """Transfer the string equation."""
    for i in range(0,len(stri)):
        if (stri[i].isdigit()):
            return i , stri[i]

def absd(num1,num2):
    """Calculate the absolute difference between two numbers."""
    return abs(num1-num2)

def wait(num):
    """Wait for a specified number of seconds."""
    play_audio(r'C:\Users\Matan\Downloads\DrumRoll.mp3')
    time.sleep(num)

from setuptools import setup, find_packages

setup(
    name='Matan''sLIB',
    version='0.1.0',
    description='A library for random things',
    packages=find_packages(),
    install_requires=[
        'pydub',
    ],
    python_requires='>=3.6',
    author='That One Indian Kido',
)