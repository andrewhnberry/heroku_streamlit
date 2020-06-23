# Important Plugins
import streamlit as st #start off my loading streamlit

# importing Newspaper3k
import newspaper
from newspaper import Article

# Custom Functions
#---------------------------------

#article downloader
def run_api(user_url_input):
    article = Article(user_url_input)
    article.download()
    article.parse()
    article.nlp()
    return meta_extraction(article)

#article meta extraction + summarizer
def meta_extraction(article):
    st.write('**The title of this article is ** ' + article.title)
    st.write('**The author of this article is **' + str(article.authors))
    st.write('**The published date of this article is **' + str(article.publish_date))
    st.write('**The source of this article is **' + article.source_url)

    st.write('## Top Keywords of this Article Below:')
    st.write(str(article.keywords))
    st.write('## Summary of Article Below:')
    st.write(article.summary)
    return


# Page Design
#-------------------------------
st.markdown('# This Streamlit application will scrape, display some meta data, and summarize articles.')

# Text Input
user_url_input = st.text_input("Please enter the URL of article")

# Button to Run the script
if st.button('Summarize the Article'):
    st.write(run_api(user_url_input))
else:
    st.write(st.markdown('**Button not yet executed.**'))
