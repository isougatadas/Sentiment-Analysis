import streamlit as st  
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analysis", 
page_icon=":shark:", 
layout="centered", 
initial_sidebar_state="auto", 
menu_items=None)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


def main():
	st.title("Sentiment Analysis")
	menu = ["Analyzer"]

	if menu:
		st.write("Type anything below and analyze the sentiment of the text.")
		with st.form(key='nlpForm'):
			raw_text = st.text_area("", placeholder="Enter text here...")
			submit_button = st.form_submit_button(label='Analyze')

		col1 = st.columns(1)
		if submit_button:
				st.info("Results")
				sentiment = TextBlob(raw_text).sentiment

				if sentiment.polarity > 0:
					st.subheader("Sentiment: :smiley: _*Positive*_ :smiley: ")
				elif sentiment.polarity < 0:
					st.subheader("Sentiment: :angry: _*Negative*_ :angry: ")
				else:
					st.subheader("Sentiment: 🤔 _*Neutral*_ 🤔 ")
	else:
		st.subheader("How Sentiment Analysis works?")


if __name__ == '__main__':
	main()