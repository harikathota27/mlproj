import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)


model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))


def main():
	st.title("SMS Spam Classifier")
	msg=st.text_area("Enter the message")
	if st.button("Predict"):
		print(msg)
		print(type(msg))
		data = [msg]
		print(data)
		vec = cv.transform(data).toarray()
		result = model.predict(vec)
		if result[0] == 0:
			st.success("This is not a Spam Message")
			speak("This is not a Spam Message")
		else:
			st.error("This is a Spam Message")
			speak("This is a Spam Message")
main()