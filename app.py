import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

df =pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title("India's Data Visualization")

selected_state = st.sidebar.selectbox('Select State',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')
if plot == True:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',zoom=4, size = primary, color = secondary,
                                size_max = 35, mapbox_style ='carto-positron', width=1200, height=700,
                                color_continuous_scale = 'plasma', hover_name = 'District')
        st.plotly_chart(fig, use_container_width=True)
    else :
        # plot for state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',zoom=4, size = primary, color = secondary,
                                size_max = 35, mapbox_style = 'carto-positron', width=1200, height=700,
                                color_continuous_scale='plasma', hover_name = 'District'
                                )
        st.plotly_chart(fig, use_container_width=True)
