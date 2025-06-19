import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox & subheader
st.title('Weather Forecast for the Next Days')
place = st.text_input('Place')
days = st.slider('Forecast Days', max_value=5, min_value=1,
                  help='Select the days you want to see forecasted.')
option = st.selectbox('Select data to view',
                      options=('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

if place:
    # Get the temperature & sky data
    filtered_data = get_data(place=place, forecast_date=days)

    if option == 'Temperature':
        # Create temperature plot
        temperature = [dict['main']['temp']/10 for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=dates,y=temperature,labels={'x' : 'Dates','y' : 'Temperature(C)'})
        st.plotly_chart(figure)

    if option == 'Sky':
        images = {'Clear':'images/clear.png',
                  'Clouds':'images/cloud.png',
                  'Rain':'images/rain.png',
                  'Snow':'images/snow.png'}
        sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_condition]
        st.image(image_path,width=115)