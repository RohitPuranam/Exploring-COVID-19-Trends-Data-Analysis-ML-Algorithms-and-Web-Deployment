import streamlit as st
import pandas as pd
import pickle
from Main import main

pickle_in = open("COVID-19_Analysis.pkl", "rb")
classifier = pickle.load(pickle_in)

html_temp = """
    <div style="background-color:#E4D7C8;padding:10px;border-radius:20px">
    <h2 style="color:black;text-align:center;font-family:serif;">
    Welcome to COVID-19 Diagnosis System</h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/2383010/pexels-photo-2383010.jpeg?cs=srgb&dl=pexels-total-shape-2383010.jpg&fm=jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()

st.write("""### Please select a format in which you want to provide details""")

select_type = st.selectbox("", ("Drop file", "Fill Details"))


if select_type == "Drop file":
    st.write("You can drop a file here")
    uploaded_file = st.file_uploader("", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        res = classifier.predict(data)
        if res[res == '1']:
            st.info("""### The Result of the COVID-19 test is: POSITIVE""")
        elif res[res == '0']:
            st.info("""### The Result of the COVID-19 test is: NEGATIVE""")
        else:
            st.info("""### INVALID DATA """)

elif select_type == "Fill Details":
    main()
else:
    st.error("Please choose a correct type")

