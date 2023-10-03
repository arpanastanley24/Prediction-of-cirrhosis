import streamlit as st
import pickle
import numpy as np

# Load the model, scaler and encoder
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('StandardScaler.pkl', 'rb') as f:
    StandardScaler = pickle.load(f)


# Create the input form for the user
st.title('Cirrhosis disease Prediction')
st.write('Please fill in the following details:')

N_Days = st.number_input('N_Days', min_value=41, max_value=4795, step=1)

Age = st.number_input('Age', min_value=9598, max_value=28650, step=1)

Ascites = st.selectbox('Ascites', ['Yes', 'No'])

Hepatomegaly = st.selectbox('Hepatomegaly', ['Yes', 'No'])

Spiders = st.selectbox('Spiders', ['Yes', 'No'])

Edema = st.selectbox('Edema', ['no edema and no diuretic therapy for edema',
                               'edema present without diuretics, or edema resolved by diuretics',
                               'edema despite diuretic therapy'])

Albumin = st.number_input('Albumin', min_value=1, max_value=5, step=1)

Copper = st.number_input('Copper', min_value=4, max_value=588, step=1)

Platelets = st.number_input('Platelets', min_value=62, max_value=721, step=1)

Prothrombin = st.number_input('Prothrombin', min_value=9, max_value=18, step=1)


# Encode the Gender feature
if Ascites == 'Yes':
    Ascites = 1
else:
    Ascites = 0

if Hepatomegaly == 'Yes':
    Hepatomegaly = 1
else:
    Hepatomegaly = 0

if Spiders == 'Yes':
    Spiders = 1
else:
    Spiders = 0

if Edema == 'no edema and no diuretic therapy for edema':
    Edema = 0
elif Edema == 'edema present without diuretics, or edema resolved by diuretics':
    Edema = 1
else:
    Edema = 2

input_data = [[N_Days, Age, Ascites, Hepatomegaly, Spiders, Edema, Albumin, Copper, Platelets, Prothrombin]]

input_data = np.array(input_data)

st.write(input_data)

scaled_data = StandardScaler.transform(input_data)

# Make the prediction
prediction = model.predict(scaled_data)[0]

# Convert prediction to string output
result = f'the stage of cirrhosis disease is {prediction}'

# Create submit button to display prediction
if st.button('Submit'):
    st.write(f'The predicted result is: {result}')