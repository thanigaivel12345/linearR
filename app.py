import streamlit as st

st.title("IPL win Prediction")

teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah','Mohali', 'Bengaluru']




import pickle

pipe=pickle.load(open('THANIGAIVEL.pickle','rb'))

st.title("IPL win Prediction")

col1, col2 = st.columns(2)

with col1:
    batting_team=st.selectbox('select the batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('select th bowling team',sorted(teams))

selected_city=st.selectbox('select host city',sorted(cities))

target=st.number_input('target')
