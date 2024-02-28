import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("COVID-19_Analysis.pkl", "rb")
classifier = pickle.load(pickle_in)


def predict_copd(Breathing_Problem, Fever, Dry_Cough, Sore_throat, Running_Nose, Asthma, Chronic_Lung_Disease, Headache,
                 Heart_Disease,	Diabetes, Hyper_Tension, Fatigue , Gastrointestinal , Abroad_travel,
                 Contact_with_COVID_Patient, Attended_Large_Gathering, Visited_Public_Exposed_Places,
                 Family_working_in_Public_Exposed_Places):

    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Breathing_Problem
        in: query
        type: number
        required: true
      - name: Fever
        in: query
        type: number
        required: true
      - name: Dry_Cough
        in: query
        type: number
        required: true
      - name: Sore_throat
        in: query
        type: number
        required: true
      - name: Running_Nose
        in: query
        type: number
        required: true
      - name: Asthma
        in: query
        type: number
        required: true
      - name: Chronic_Lung_Disease
        in: query
        type: number
        required: true
      - name: Headache
        in: query
        type: number
        required: true
      - name: Heart_Disease
        in: query
        type: number
        required: true
      - name: Diabetes
        in: query
        type: number
        required: true
      - name: Hyper_Tension
        in: query
        type: number
        required: true
      - name: Fatigue
        in: query
        type: number
        required: true
      - name: Gastrointestinal
        in: query
        type: number
        required: true
      - name: Abroad_travel
        in: query
        type: number
        required: true
      - name: Contact_with_COVID_Patient
        in: query
        type: number
        required: true
      - name: Attended_Large_Gathering
        in: query
        type: number
        required: true
      - name: Visited_Public_Exposed_Places
        in: query
        type: number
        required: true
      - name: Family_working_in_Public_Exposed_Places
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    prediction = classifier.predict([[Breathing_Problem, Fever, Dry_Cough, Sore_throat, Running_Nose, Asthma, Chronic_Lung_Disease, Headache,
                 Heart_Disease,	Diabetes, Hyper_Tension, Fatigue , Gastrointestinal , Abroad_travel,
                 Contact_with_COVID_Patient, Attended_Large_Gathering, Visited_Public_Exposed_Places,
                 Family_working_in_Public_Exposed_Places]])
    print(prediction)
    return prediction


def main():
    html_temp = """
    <div style="background-color:lavender;padding:10px;border-radius:20px">
    <h2 style="color:black;text-align:center;font-family:serif">Need Some Details for Predicting the Disease</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Breathing_Problem = st.text_input("Breathing_Problem", max_chars=3, placeholder="Breathing_Problem")
    Fever = st.text_input("Fever", max_chars=1, placeholder="Fever")
    Dry_Cough = st.text_input("Dry_Cough", placeholder="Dry_Cough")
    Sore_throat = st.text_input("Sore_throat", max_chars=3, placeholder="Sore_throat")
    Running_Nose = st.text_input("Running_Nose", max_chars=3, placeholder="Running_Nose")
    Asthma = st.text_input("Asthma", placeholder="Asthma")
    Chronic_Lung_Disease = st.text_input("Chronic_Lung_Disease", placeholder="Chronic_Lung_Disease")
    Headache = st.text_input("Headache", placeholder="Headache")
    Heart_Disease = st.text_input("Heart_Disease", placeholder="Heart_Disease")
    Diabetes = st.text_input("Diabetes", placeholder="Diabetes")
    Hyper_Tension = st.text_input("Hyper_Tension", placeholder="Hyper_Tension")
    Fatigue  = st.text_input("Fatigue", placeholder="Fatigue")
    Gastrointestinal  = st.text_input("Gastrointestinal", placeholder="Gastrointestinal")
    Abroad_travel = st.text_input("Abroad_travel", placeholder="Abroad_travel")
    Contact_with_COVID_Patient = st.text_input("Contact_with_COVID_Patient", placeholder="Contact_with_COVID_Patient")
    Attended_Large_Gathering = st.text_input("Attended_Large_Gathering", placeholder="Attended_Large_Gathering")
    Visited_Public_Exposed_Places = st.text_input("Visited_Public_Exposed_Places",
                                                  placeholder="Visited_Public_Exposed_Places")
    Family_working_in_Public_Exposed_Places = st.text_input("Family_working_in_Public_Exposed_Places",
                                                  placeholder="Family_working_in_Public_Exposed_Places")

    result = ""
    if st.button("Predict"):
        result = predict_copd(Breathing_Problem, Fever, Dry_Cough, Sore_throat, Running_Nose, Asthma,
                              Chronic_Lung_Disease, Headache, Heart_Disease, Diabetes, Hyper_Tension, Fatigue ,
                              Gastrointestinal , Abroad_travel, Contact_with_COVID_Patient, Attended_Large_Gathering,
                              Visited_Public_Exposed_Places, Family_working_in_Public_Exposed_Places)
        if result[result == '1']:
            st.info("""### The Result of the COVID-19 test is: POSITIVE""")
        elif result[result == '0']:
            st.info("""### The Result of the COVID-19 test is: NEGATIVE""")
        else:
            st.info("""### INVALID DATA """)


if __name__ == '__main__':
    main()
