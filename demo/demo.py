import streamlit as st
import streamlit.components.v1 as components
st.write("Hello world")
components.html(
    """
    <body>
   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094"
     crossorigin="anonymous"></script>
<!-- ad1 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-5056338602918094"
     data-ad-slot="3075916015"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
    </body>
    """
   
)
st.write("over")
