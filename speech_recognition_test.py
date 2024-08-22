import speech_recognition as sr
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
def detect_trigger_words(text):
    trigger_words = ['help', 'save me', 'emergency']
    if any(word in text.lower() for word in trigger_words):
        return True
    return False
