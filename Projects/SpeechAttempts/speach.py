import subprocess
#import requests
text = '"Hello world"'
subprocess.call('espeak '+text, shell=True)
print(text)
text1 = '"I am doing it now"'
subprocess.call('espeak '+text1, shell=True)
import os
os.system('espeak' '"The quick brown fox"')
from tts_watson.TtsWatson import TtsWatson

ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') 
ttsWatson.play("Hello World")
