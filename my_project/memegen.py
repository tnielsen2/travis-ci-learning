import requests
import os
import json

top = 'This is only'
bottom = 'a test'


IMG_FLIP_USERNAME = os.getenv('IMG_FLIP_USERNAME')
IMG_FLIP_PASSWORD = os.getenv('IMG_FLIP_PASSWORD')


def creatememe(top, bottom):
    url = 'https://api.imgflip.com/caption_image'
    params = {
        'template_id': '102156234',
        'username': IMG_FLIP_USERNAME,
        'password': IMG_FLIP_PASSWORD,
        'text0': top,
        'text1': bottom,
    }
    try:
        res = requests.post(url, params)
    except Exception as e:
        raise Exception('Error requesting the service.')
    try:
        dict_res = json.loads(res.text)
    except:
        msg = 'Unexpected response format: (%s)' % res.text
        raise Exception(msg)
    if not dict_res['success']:
        msg = 'Unexpected response: (%s)' % res.text
        raise Exception(msg)
    return dict_res['data']['url']


memeurl = creatememe(top,bottom)

print(memeurl)