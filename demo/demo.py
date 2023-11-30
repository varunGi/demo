import streamlit as st

st.title("My Streamlit App")

adsense_code = """
    
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094"
         crossorigin="anonymous"></script>
        <!-- Your AdSense ad unit code goes here -->
   
"""
st.write(adsense_code, allow_html=True)
st.write("Hello world")
# st.write(<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094" crossorigin="anonymous"></script>,)
st.write("over end")
