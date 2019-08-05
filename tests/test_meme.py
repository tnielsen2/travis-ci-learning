import sys
import os

currentDirectory = os.getcwd()
sys.path.insert(1, currentDirectory)

from my_project import memegen

def test_url():
    meme = memegen.creatememe('this should', 'work with a test')
    print(meme)
    assert 'img' in meme
