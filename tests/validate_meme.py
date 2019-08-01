import unittest
import sys
from memegen import creatememe

pwd = myCmd = os.popen('pwd').read()
sys.path.append(pwd)

def validate_url():
    meme = creatememe('this should', 'work with a test')
    print(meme)
    assert 'img' in meme

def testassert():
    string = 'this is only a test'
    assert 'test' in string
