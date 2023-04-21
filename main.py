# Maria

from vosk import Model, KaldiRecognizer

import os
import pyaudio 


model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=payaudio.paInt16, channels=1 rate=16000, input=true, frames_per_buffer=8000)
stream.start_stream()
while True:
    data = stream.read(4000)
    if lem(data) == 0:
        break
    if rec.Acceptwaveform(data):
         print (rec.Result())
    else:
        print(rec.Result())

print (rec.FinalResult())