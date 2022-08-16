import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source:
    print("Xin chào bạn")
    print("Hãy nói thứ bạn muốn tìm.....")
    audio = r2.listen(source)
    text = r2.recognize_google(audio, language="vi-VN")
    print(text)

url = "https://www.youtube.com/results?search_query="
with sr.Microphone() as source:
    print("Bạn muốn nghe ca sĩ nào hát")
    audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio, language="vi-VN")
        print(get)
        print("Đang mở bằng youtube")

        wb.get().open_new(url+text+get)
    except sr.UnknownValueError:
        print("Lỗi")
    except sr.RequestError as e:
        print('Lỗi'.format(e))
    except:
        print("Lỗi")