import my_project

#pwd = myCmd = os.popen('pwd').read()
#sys.path.append(pwd)

def validate_url():
    meme = my_project.creatememe('this should', 'work with a test')
    print(meme)
    assert 'img' in meme

def testassert():
    string = 'this is only a test'
    assert 'test' in string
