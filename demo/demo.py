import streamlit as st
import streamlit.components.v1 as components
st.write("Hello world")
components.html(
    """
    <head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094"
     crossorigin="anonymous"></script>

    </head>
    """
   
)
st.write("over")
