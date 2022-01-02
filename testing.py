from pygame import *
import speech_recognition as s_r
# print(s_r.Microphone.list_microphone_names())
mic = s_r.Microphone(device_index=1)
print(mic)
def play_mp3(mp3filename):

    mixer.init(devicename="HyperX Quadcast")
    print(mixer.get_init())
    mixer.music.load(mp3filename)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(100)

# play_mp3("myVoice.mp3")