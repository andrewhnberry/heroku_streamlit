import streamlit as st

#importing Newspaper3k
import newspaper
from newspaper import Article

#Text Input
user_url_input = st.text_input("Enter URL of article", '')

# article Summarizer
def run_api(user_url_input):
    article = Article(user_url_input)
    article.download()
    article.parse()
    article.nlp()

    return article.summary
#
if st.button('Summarize the Article'):
    st.write(run_api(user_url_input))
else:
    st.write('no_url/not_executed')
