from my_project import memegen
#pwd = myCmd = os.popen('pwd').read()
#sys.path.append(pwd)

def test_url():
    meme = memegen.creatememe('this should', 'work with a test')
    print(meme)
    assert 'img' in meme
