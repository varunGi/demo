import streamlit as st
import streamlit.components.v1 as components
st.title("My Streamlit App")


html_string = "
               <head>
               <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094"
     crossorigin="anonymous"></script>
               </head>"

st.markdown(html_string, unsafe_allow_html=True)
