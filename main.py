import streamlit as st
from scrape import (scrape_website, split_dom_content, clean_body_content, extract_body_content)

st.title("AI Web Scraper")
url= st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("scraping")
    result=scrape_website(url)
    #need to figure out a way to implement IP ban, captcha and honepot bypasses
    body_content=extract_body_content(result)
    cleaned_content= clean_body_content(body_content)

    st.session_state.dom_content= cleaned_content
    with st.expander("view dom content"):
        st.text_area("DOM Content", cleaned_content, height=300)

