import sounddevice
from scipy.io.wavefile import write
fs=44100
second= int(input("Duration: "))
print("Recording.....")
record_voice= sounddevice.rec(second*fs,sampleate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finish")