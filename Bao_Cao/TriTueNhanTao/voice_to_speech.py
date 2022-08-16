import speech_recognition as sr
 
def main():
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Nói gì đó")
        audio = r.listen(source)
        print("Đang ghi")
  
        try:
            print("Bạn đã nói \n" + r.recognize_google(audio))
            print("Chuyển thành công \n ")
            
        except Exception as e:
            print("Lỗi :  " + str(e))
 
        # write audio
        with open("ghi_am.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
if __name__ == "__main__":
    main()
    