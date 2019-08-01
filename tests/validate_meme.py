import unittest

import sys
sys.path.append('/Users/tnielsen/dev/travis-ci-learning')
from memegen import creatememe

def validate_url():
    meme = creatememe('this should', 'work with a test')
    print(meme)
    assert 'img' in meme

def testassert():
    string = 'this is only a test'
    assert 'test' in string
