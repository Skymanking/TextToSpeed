import gtts
from playsound import playsound
with open('Mau.txt', 'r', encoding='UTF-8') as f:
    data = f.read()
print(data)
tts = gtts.gTTS(data, lang="vi")
tts.save("hello.mp3")
f.close()

