# @Author: Dhaval Patel Copyrights Codebasics Inc. and LearnerX Pvt Ltd.

import streamlit as st
from rag import process_urls, generate_answer

st.title("Real Estate Research Tool")

url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

if "urls_processed" not in st.session_state:
    st.session_state["urls_processed"] = False

status_box = st.empty()

process_url_button = st.sidebar.button("Process URLs")
if process_url_button:
    urls = [url for url in (url1, url2, url3) if url!='']
    if len(urls) == 0:
        st.session_state["urls_processed"] = False
        status_box.text("You must provide at least one valid url")
    else:
        try:
            for status in process_urls(urls):
                status_box.text(status)
            st.session_state["urls_processed"] = True
        except Exception as e:
            st.session_state["urls_processed"] = False
            status_box.error(f"Failed to process URLs: {str(e)}")

query = st.text_input("Question")
if query:
    if not st.session_state["urls_processed"]:
        status_box.text("Please process at least one URL first.")
    else:
        try:
            answer, sources = generate_answer(query)
            st.header("Answer:")
            st.write(answer)

            if sources:
                st.subheader("Sources:")
                for source in sources.split("\n"):
                    st.write(source)
        except Exception as e:
            status_box.error(f"Failed to generate answer: {str(e)}")
