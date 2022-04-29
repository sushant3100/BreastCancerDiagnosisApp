
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
import webbrowser

def classification(input_data):
    #load classifier
    classifier = pickle.load(open("bc_pred.sav", 'rb'))
    pred=[]
    prediction = classifier.predict(input_data)
    #st.header('**Prediction Output**')
    for i in prediction:
        if i == 'B':
            pred.append('Benign: No cancer found.')
            #print('Benign: No cancer found')
        else:
            pred.append('Malignant: Cancer detected. Futher classification of subytpes required.')
            #print('Malignant: Cancer detected')
    return pred

image = Image.open('bc.jpg')
st.image(image, use_column_width=True)
st.markdown("""
            # Breast Cancer Prediction
            This app can classify a breast cancer tumor into Benign or Malignant

            Developed by: Sushant, Purva, Rutwik
            """)

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['csv'])
    st.sidebar.markdown(""" 
                        [Example input file](https://drive.google.com/file/d/1MkJJL0Tz2iUIi4k-el6D57baq7Ht-iSf/view?usp=sharing)
    """)

if st.sidebar.button('Predict'):
    load_data = pd.read_csv(uploaded_file, header=None)
    st.header('**Original input data**')
    st.write(load_data)
    load_data = load_data.values
    st.header('**Prediction**')
    predictions = classification(load_data)
    st.markdown(predictions)
else:
    st.info('Upload input data in the sidebar to start!')

with st.sidebar.header('2. Breast Cancer Subtypes Prediction'):
    st.sidebar.markdown("""
                        [Press button for subtype prediction](https://sushantbioinformatics.shinyapps.io/app-bcsubtypes/)
    """)
    url = 'https://sushantbioinformatics.shinyapps.io/app-bcsubtypes/'
    if st.sidebar.button('Subtypes'):
        webbrowser.open_new_tab(url)