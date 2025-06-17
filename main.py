import streamlit as st
import plotly.express as px


st.title('Weather Forecast for the Next Days')
place = st.text_input('Place')
days = st.slider('Forecast Days', max_value=5, min_value=1,
                  help='Select the days you want to see forecasted.')
option = st.selectbox('Select data to view',
                      options=('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

def get_data(days):
    dates = ['2025-24-10','2025-25-10','2025-27-10']
    temperature  = [10, 12, 15]
    temperature = [i * days for i in temperature]
    return dates, temperature

dates, temperature = get_data(days)

figure = px.line(x=dates,y=temperature,labels={'x' : 'Dates','y' : 'Temperature(C)'})
st.plotly_chart(figure)