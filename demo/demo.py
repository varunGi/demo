import streamlit as st
st.markdown(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5056338602918094"
     crossorigin="anonymous"></script>


    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoML")
    choice = st.radio("Navigation",
                      ["Introduction", "Upload", "Cleaning", "Profiling", "Data visualization", "Modelling",
                       "Download"])
if choice == "Introduction":

    st.write("# Welcome to machine learning project platform! 👋")
    st.markdown("""
    At our website, we offer a comprehensive suite of tools and features to assist you in your data-driven projects. Whether you're a data enthusiast, a business analyst, or a machine learning practitioner, our platform is designed to streamline your workflow and help you make insightful decisions from your data.
    
    ### *Upload:*
    In this section, you can effortlessly upload your dataset and explore its contents. Once your data is uploaded, our platform provides a detailed description of the dataset, highlighting key statistics, such as the number of rows, columns, and unique values. You can quickly identify potential data quality issues by checking for the presence of duplicate records and missing values in each column.
    """)
