# Maria

from vosk import model, KaldiRecognizer

import os
import pyaudio 


model = model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.Acceptwaveform(data):
         print (rec.Result())
    else:
        print(rec.Result())

print (rec.FinalResult())