import streamlit as st
import streamlit.components.v1 as components
st.title("My Streamlit App")
ad_code=""" <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094"
     crossorigin="anonymous"></script>
<!-- ad2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-5056338602918094"
     data-ad-slot="4692551330"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
     """
components.html(ad_code)
st.write("Hello world")
# st.write(<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094" crossorigin="anonymous"></script>,)
st.write("over end")