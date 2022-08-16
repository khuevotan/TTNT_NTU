import os
import random
from time import ctime
import time
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import playsound

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="vi-VN")
        except sr.UnknownValueError:
            speak('Xin lỗi, tôi không hiểu bạn đang nói gì')
        except sr.RequestError:
            speak('Xin lỗi, âm thanh không hoạt động')
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='vi')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def response(voice_data):
    if 'tên' in voice_data:
        speak('Tôi là giả lập trợ lý ảo python')
    if 'giờ' in voice_data:
        speak(ctime())
    if 'tìm kiếm' in voice_data:
        search = record_audio('Bạn muốn tìm kiếm điều gì?')
        url = 'http://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Đây là kết quả tìm kiếm được cho yêu cầu ' + search)
    if 'vị trí' in voice_data:
        location = record_audio('Bạn muốn tìm nơi nào trên google map?')
        url = 'https://www.google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Đây là vị trí của ' + location)
    if 'tạm biệt' in voice_data:
        speak("Tạm biệt, chúc bạn có một ngày tốt lành")
        exit()


time.sleep(1)
speak('Tôi có thể giúp gì được cho bạn')
while True:
    voice_data = record_audio()
    response(voice_data)
