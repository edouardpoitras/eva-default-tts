"""
Assumes a working docker instance of the parente/espeakbox image.
This should be the case with the docker-compose method of installing Eva.
"""
import sys
import requests
import gossip
from eva import log
from eva import conf

def get_settings_string():
    """
    Will eventually pull from Eva configs.

    /speech?text=<utterance>
            [&pitch=<0,99; default 50>]
            [&rate=<80,450; default 175 wpm>]
            [&voice=<name; default en>]
            [&encoding=<mp3|opus; default mp3>]
    """
    pitch = conf['plugins']['default_tts']['config']['pitch']
    rate = conf['plugins']['default_tts']['config']['rate']
    voice = conf['plugins']['default_tts']['config']['voice']
    encoding = conf['plugins']['default_tts']['config']['encoding']
    settings_string = '&pitch=' + str(pitch) + \
                      '&rate=' + str(rate) + \
                      '&voice=' + voice + \
                      '&encoding=' + encoding
    return settings_string

def tts(text):
    host = conf['plugins']['default_tts']['config']['tts_host']
    port = conf['plugins']['default_tts']['config']['tts_port']
    try:
        r = requests.get('http://' + host + ':' + str(port) + '/speech?text=' + text + get_settings_string())
        return {'audio': r.content, 'content-type': r.headers['content-type']}
    except Exception:
        log.error('Could not connect to default text-to-speech service: %s' %sys.exc_info()[1])
        return {'audio': None}

@gossip.register('eva.text_to_speech', provides=['default_tts'])
def text_to_speech(context):
    try:
        response = tts(context.get_output_text())
        context.set_output_audio(response['audio'], response['content-type'])
    except:
        log.error('Could not convert text to speech with default_tts')
