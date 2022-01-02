import keyboard
from gtts import gTTS
from pygame import *
from pynput.keyboard import  *

def create_voice_recorded(txt: str, lang: str = "es", tld: str = "es"):
    print(txt)
    recorded = gTTS(text=txt, lang=lang, slow=True, tld=tld)
    filename = "myVoice.mp3"
    recorded.save(filename)
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(100)


isCaptureText = False
message = ""

def press_on(key):

    global isCaptureText
    global message
    if key == Key.enter:
        if isCaptureText == False:
            isCaptureText = True
        else:
            isCaptureText = False
            create_voice_recorded(message)
    else:
        if isCaptureText:
            if key == Key.space:
                message += " "
            else:
                message += str(key.char)

def press_of(key):
    if key == Key.esc:
        return False

with Listener(on_press = press_on, on_release = press_of) as listener:
        listener.join()
